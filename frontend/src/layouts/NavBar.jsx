import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
// import '../styles/layouts/NavBar.css'
import BrandName from "../components/common/BrandName";
import {
  NavBarDiv,
  NavBarLi,
  NavBarUl,
  NavLinkA,
  NavBarButton,
} from "../styles/layouts/NavBar";
import MobileMenuIcon from "../components/common/MobileMenuIcon";
import { FaUserCircle } from "react-icons/fa";

const NavBar = () => {
  const navigate = useNavigate();
  const handleLoginClick = () => {
    if (!LogInState) {
      navigate("/login");
    }
  };

  const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
  const toggleMobileMenu = () => {
    setMobileMenuOpen(!mobileMenuOpen);
  };

  const [LogInState, setLogInState] = useState(false);
  //Here change the useState parameter to a login state input

  const brandColor = "#ffffff";

  return (
    <NavBarDiv>
      <NavBarUl>
        <BrandName color={brandColor} />
        <MobileMenuIcon onClick={toggleMobileMenu} />
        <NavBarLi isVisible={mobileMenuOpen}>
          <NavLinkA to="/">HOME</NavLinkA>
        </NavBarLi>
        <NavBarLi isVisible={mobileMenuOpen}>
          <NavLinkA to="/Support">SUPPORT</NavLinkA>
        </NavBarLi>
        <NavBarLi isVisible={mobileMenuOpen}>
          <NavLinkA to="ContactUs">CONTACT</NavLinkA>
        </NavBarLi>
        {/* <button className='logInButton'>LOG IN</button>  */}
      </NavBarUl>
      <NavBarButton
        as="button"
        onClick={handleLoginClick}
        isVisible={mobileMenuOpen}
      >
        {LogInState ? <FaUserCircle size={40} /> : "Log In"}
      </NavBarButton>
    </NavBarDiv>
  );
};

export default NavBar;

// // Navbar.js

// import React from 'react';
