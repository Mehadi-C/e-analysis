import React from 'react';
// import React, {useState,useEffect} from 'react';
// import logo from './logo.svg';
import './App.css';
import Upload from './components/upload/Upload'


function App(){
  return (
    <div className="App">
        <Upload/>
    </div>
  );
}

// function App() {
//   const [currentTime, setCurrentTime] = useState(0);

//   useEffect(() => {
//     fetch('/time').then(res => res.json()).then(data => {
//       setCurrentTime(data.time);
//     });
//   }, []);
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Esports Analysis
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Valorant and Overwatch 2 and CSGO and League
//         </a>
//         <p>The current time is {currentTime}.</p>
//       </header>
//     </div>
//   );
// }

export default App;
