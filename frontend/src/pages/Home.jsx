import HomeBody from '../components/pages/HomeBody';
import NavBar from '../layouts/NavBar';
import { HomeDiv } from '../styles/components/HomeBody';

function Home() {
  return (
    <HomeDiv>
      <NavBar/>
      <HomeBody/>
    </HomeDiv>
  );
}

export default Home;
