import React, {useState,useEffect, Component} from 'react';
import logo from './logo.svg';
import './App.css';
import Main from './components/Main.js';

class App extends Component {
  state= {
    src: ''
}

  render(){
  return (
    <div >
      <header>
        <Main />
      </header>
    </div>
  );
  }
}

export default App;