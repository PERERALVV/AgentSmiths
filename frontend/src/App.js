import './App.css';
import './home.css';
import NavBar from './NavBar';
import HomePage from './HomePage';

function App() {
  return (
    <div className="App">
      <header className="App-header">
      <NavBar/>
      </header>
      <HomePage/>
    </div>
  );
}

export default App;
