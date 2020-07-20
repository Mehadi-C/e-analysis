import React, {useState,useEffect, Component} from 'react';
import logo from './logo.svg';
import './App.css';
import Main from './components/Main.js';

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
    <div >
      <header>
        {/* <div className="input-field">
          <input type="text" id="src" onChange={this.handleChange}/>
        </div>
        <img src={this.state.src} width="800" height="500" /> */}
        <Main />
      </header>
    </div>
  );
  }
}

export default App;