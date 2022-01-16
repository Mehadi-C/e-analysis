import React,{useState} from 'react';
import ReactPlayer from 'react-player'
import './Upload.css';
import axios from 'axios';
import Dropzone from 'react-dropzone';



const Upload=()=>{
    const [controls,setControls]=useState(true);
    const [image,setImage]=useState('');
    const [video,setVideo]=useState('');
    const maxSize = 30 * 1024 * 1024
    function sendtoserver(files){
        let formData=new FormData();
        formData.append('file',files[0]);
        console.log(files)
        const options={}
        
        axios.post('http://127.0.0.1:5000/api',formData,options).then(res=>
        { 
                console.log(res)
                setTimeout(()=>{
                    console.log(res.data.img);
                    if(res.data.img !== undefined){
                        setImage('http://127.0.0.1:5000/img/'+res.data.img);
                    }
                    if(res.data.vid !== undefined){
                        setVideo('http://127.0.0.1:5000/img/'+res.data.vid);
                    }
                },2000)
        }
        ).catch((err)=>{
            console.log(err);
        });
    
    }
    const onDrop=(acceptedFiles)=>{
        sendtoserver(acceptedFiles)
    }
    const handleOnSubmit=  ({target:{files}})=>{
        sendtoserver(files)
    }
    
    return(
        <>
        {
            (
                
                <div className="container">
                {
                    (
                    <>
                        <h3>Upload Image or Video</h3>
                        <Dropzone onDrop={onDrop} multiple={false} maxSize={maxSize}>
                            {
                                ({ getRootProps,getInputProps })=>(
                                    <div {...getRootProps({ className: "file-container" })} onChange={handleOnSubmit}>
                                        <input {...getInputProps()} />
                                        {/* <img src={Image} alt="example"/> */}
                                        <p>Drop Image or Video Here </p>
                                        <input type="file"  onChange={handleOnSubmit} name="upfile"/>
                                    </div>
                                )
                            }
                           
                        </Dropzone>
                        
                     </>  
                    )
                }
    
             </div>
            )
        }       
        <div className="content">
            <h4>Result:</h4>
            <img src={image}/>
            <ReactPlayer url={video} controls={controls} width='100%' height='100%'/>
        </div>
         </>
    )
};

export default Upload;