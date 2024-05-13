import React from 'react';
import { BrowserRouter, Link } from 'react-router-dom';
// import '../styles/layouts/NavBar.css'
import BrandName from '../components/common/BrandName';
import { NavBarDiv, NavBarLi, NavBarUl, NavLinkA, NavBarButton } from '../styles/layouts/NavBar';

const NavBar = () => {
  const brandColor = "#ffffff"; 
  return (
    <BrowserRouter>
      <NavBarDiv>
          <NavBarUl>
              <NavBarLi>
                <BrandName color={brandColor}/>
              </NavBarLi>
              <NavBarLi>
                <NavLinkA to="#">HOME</NavLinkA>
              </NavBarLi>
              <NavBarLi>
                <NavLinkA to="#">SUPPORT</NavLinkA>
              </NavBarLi>
              <NavBarLi>
                <NavLinkA to="#">SERVICE PLANS</NavLinkA>
              </NavBarLi>
              <NavBarLi>
                <NavLinkA to="#">CONTACT</NavLinkA>
              </NavBarLi>
              {/* <button className='logInButton'>LOG IN</button>  */}
          </NavBarUl>
          <NavBarButton>LOG IN</NavBarButton> 
      </NavBarDiv>
    </BrowserRouter>
  );
};

export default NavBar;

// // Navbar.js

// import React from 'react';
