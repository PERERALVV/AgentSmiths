import React from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
  return (
    <nav className='NavBar-nav'>
        <Link to="" className='Brand'>AgentSmiths</Link>
        <ul>
            <li>
            <Link to="" className='NavLink'>HOME</Link>
            </li>
            <li>
            <Link to="" className='NavLink'>SUPPORT</Link>
            </li>
            <li>
            <Link to="" className='NavLink'>SERVICE PLANS</Link>
            </li>
            <li>
            <Link to="" className='NavLink'>CONTACT</Link>
            </li>
        </ul>
        <button className='logInButton'>LOG IN</button> 
    </nav>
  );
};

export default NavBar;

// // Navbar.js

// import React from 'react';
