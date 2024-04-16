import './App.css';
import React from 'react';

import './home.css';
import NavBar from './NavBar';
import HomePage from './HomePage';
import Login from './pages/Login';
function App() {
  return (
    <div className="App">
      <header className="App-header">
      {/*<NavBar/>
      </header>
  <HomePage/>*/}
    <Login/>
    </header>
    </div>
  );
}

export default App;
