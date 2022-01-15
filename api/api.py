from cgitb import reset
from tabnanny import check
import time
import os
import process
import sys
import shutil
from flask import Flask, flash, request, redirect, url_for, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'originals'
DOWNLOAD_FOLDER = 'processed'
img_always = {'bmp', 'dib','pbm', 'pgm', 'ppm', 'pxm', 'pnm' , 'sr', 'ras' ,'hdr', 'pic'}
img_maybe = {'tiff', 'tif', 'exr', 'jpeg', 'jpg', 'jpe', 'jp2', 'png', 'webp'} 
vid_ext = {'avi','mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['LOWSTORAGE'] = True
app.config['MAXSIZE_MB'] = 25

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

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if(app.config['LOWSTORAGE']):
        reset_folder()

    #Uploading a file
    if request.method == 'POST':
        
        #No file
        if 'file' not in request.files:
            #flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        size = get_filesize(file)
        if file.filename == '':
            #flash('No selected file')
            return redirect(request.url)
        elif not file:
            #flash('Not file??')
            return redirect(request.url)
        elif (size > app.config['MAXSIZE_MB']*1000*1000):
            #flash('FILE TOO LARGE')
            return 'FILE TOO LARGE'
        #If File is an image
        elif  ((check_file(file.filename)==1) | (check_file(file.filename)==0)):           
            #Make unique path
            import secrets
            id = secrets.token_urlsafe(16)
            path = 'storage'+'/'+id
            res = os.path.isdir(path)
            while res:
                id = secrets.token_urlsafe(16)
                path = 'storage'+'/'+id
                res = os.path.isdir(path)
            os.mkdir(path)


            #Get filename
            filename = secure_filename(file.filename)
            upload_path = os.path.join(path, filename)
            file.save(upload_path)

            #Process and save images
            res = process.check_image(upload_path)
            #Delete original and write processed image
            process.cv2.imwrite(upload_path,res)
            
            #return send_file(res)
            return send_file(upload_path)
        
        #If file is video
        if ((check_file(file.filename)==2)):
            #Make unique path
            import secrets
            id = secrets.token_urlsafe(16)
            path = 'storage'+'/'+id
            res = os.path.isdir(path)
            while res:
                id = secrets.token_urlsafe(16)
                path = 'storage'+'/'+id
                res = os.path.isdir(path)
            os.mkdir(path)


            #Get filename
            filename = secure_filename(file.filename)
            upload_path = os.path.join(path, filename)
            file.save(upload_path)

            #Process and save images
            res = process.mkvid(upload_path,path)
            #Delete original and write processed image
            #process.cv2.imwrite(upload_path,res)
            
            #return send_file(res)
            return send_file(res)

            #return 'File Upload Success'
            #return redirect('/image')
            #return redirect(url_for('upload_file',filename=filename))

        #If File is a video
        #TODO


    #API Test: Upload UI
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


if __name__ == "__main__":
    app.run()