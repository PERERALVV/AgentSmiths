import '../styles/pages/ChatInterface.css';
import '../styles/layouts/NavBar.css';
import '../styles/components/HomeBody.css';
import NavBar from '../layouts/NavBar';
import HomeBody from '../components/pages/HomeBody';

function Home() {
  return (
    <div className="App">
      <header className="App-header">
      <NavBar/>
      </header>
      <HomeBody/>
    </div>
  );
}

export default Home;
