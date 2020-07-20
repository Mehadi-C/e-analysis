import React from 'react';

class Main extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      imageURL: 'http://localhost:5000/get-image',
    };

    this.handleUploadImage = this.handleUploadImage.bind(this);
  }

  handleUploadImage(ev) {
    ev.preventDefault();

    const data = new FormData();
    data.append('file', this.uploadInput.files[0]);
    data.append('filename', this.fileName.value);

    fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: data,
    }).then((response) => {
      response.json().then((body) => {
        this.setState({ imageURL: `http://localhost:5000/${body.file}` });
      });
    });
  }
  getImage(ev){
    ev.preventDefault();


    fetch('http://localhost:5000/get-image', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      },
    }).then((response) => {
      this.setState({ src: `http://localhost:5000/get-image` });
    })
  }

  render() {
    return (
      <div>
        <form onSubmit={this.handleUploadImage}>
          <div>
            <input ref={(ref) => { this.uploadInput = ref; }} type="file" />
          </div>
          <div>
            <input ref={(ref) => { this.fileName = ref; }} type="text" placeholder="Enter the desired name of file" />
          </div>
          <br />
          <div>
            <button>Upload</button>
          </div>
          <img src={this.state.imageURL} alt="img" />
        </form>
        <button onClick={this.getImage}>okayokay</button>
      </div>
    );
  }
}

export default Main;