import React, {useState,useEffect, Component} from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {
  state= {
    src: ''
}
handleChange = (e) => {
    this.setState ({
        [e.target.id]: e.target.value
    })
    console.log(this.state)
}
handleSubmit = (e) => {
    e.preventDefault()
    console.log(this.state)
}
  render(){
  return (
    <div className="App">
      <header className="App-header">
        <div className="input-field">
          <input type="text" id="src" onChange={this.handleChange}/>
        </div>
        <img src={this.state.src} width="800" height="500" />
      </header>
    </div>
  );
  }
}

export default App;