import os
import logging
from flask import Flask, flash, request, redirect, url_for, session, send_file, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS, cross_origin
import flask_cors 
import process 
import secrets
import shutil


UPLOAD_FOLDER = 'storage'
DOWNLOAD_FOLDER = 'processed'
img_always = {'bmp', 'dib','pbm', 'pgm', 'ppm', 'pxm', 'pnm' , 'sr', 'ras' ,'hdr', 'pic'}
img_maybe = {'tiff', 'tif', 'exr', 'jpeg', 'jpg', 'jpe', 'jp2', 'png', 'webp'} 
vid_ext = {'avi','mp4'}

app = Flask(__name__,static_folder='build',static_url_path='')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['LOWSTORAGE'] = True
app.config['MAXSTORAGE'] = 30 * 1024 * 1024
app.config['MAX_CONTENT_LENGTH'] = 30 * 1024 * 1024

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)
app.logger.info("START")

def check_file(filename):
    result = -2
    #Check for extension
    if('.' not in filename):
        result = -1 #No extension    
    elif(filename.rsplit('.', 1)[1].lower() in img_always):
        result = 0 #Image: always
    elif(filename.rsplit('.', 1)[1].lower() in img_maybe):
        result = 1 #Image: maybe
    elif(filename.rsplit('.', 1)[1].lower() in vid_ext):
        result = 2 #Image: maybe
    return result #Bad extension

def reset_folder():
    #Remove storage folder to stay in size limit
    path = 'storage/'
    shutil.rmtree(path)
    os.mkdir(path)

def get_filesize(file):
    file = request.files['file']
    file.seek(0, os.SEEK_END)
    file_length = file.tell()
    return file_length

@app.route('/img/<id>', methods=['GET'])
def getfile(id):
    path = app.config['UPLOAD_FOLDER'] + '/' + id + '/'
    file = os.listdir(path)
    print(file)
    return send_file(path+file[0])

@app.route('/img/<id>/img.webm', methods=['GET'])
def getvid(id):
    path = app.config['UPLOAD_FOLDER'] + '/' + id + '/'
    file = os.listdir(path)
    print(file)
    return send_file(path+file[0])

@app.route('/api', methods=['POST'])
def fileUpload():
    app.logger.info(str(os.listdir()))
    if(app.config['LOWSTORAGE']):
        reset_folder()
    #Setup destination
    app.logger.info(str(os.listdir()))
    id = secrets.token_urlsafe(16)
    target=UPLOAD_FOLDER + '/' + id
    res = os.path.isdir(target)
    while res:
        id = secrets.token_urlsafe(16)
        target = 'storage'+'/'+id
        res = os.path.isdir(target)
    os.mkdir(target)

    file = request.files['file']
    filename = 'img.' + file.filename.rsplit('.', 1)[1].lower()
    destination="/".join([target, filename])
    file.save(destination)
    photo_size = os.stat(destination).st_size
    if(photo_size > app.config['MAXSTORAGE']):
        shutil.rmtree(target)
    filetype = check_file(file.filename)
    #If File is an image
    if  ((filetype==1) | (filetype==0)):     
        res = process.check_image(destination)
        #Delete original and write processed image
        process.cv2.imwrite(destination,res)
        return {'img':id}
    elif ((filetype==2)):
        res = process.mkvid(destination,target)
        os.remove(destination)
        return {'vid':id}
    else:
        shutil.rmtree(target)
        return 'Invalid File'

    return {'id':id}

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run()

flask_cors.CORS(app, expose_headers='Authorization')

