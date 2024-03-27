import "./App.css";
import "./Home.css";
import NavBar from "./layouts/NavBar";
import HomePage from "./pages/Home";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <NavBar />
      </header>
      <HomePage />
    </div>
  );
}

export default App;
