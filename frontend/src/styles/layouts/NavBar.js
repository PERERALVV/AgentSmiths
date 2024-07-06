import { Link } from "react-router-dom";
import styled from "styled-components";

export const NavBarDiv = styled.nav`
  display: flex;
  // align-items: center; /* Center-align items vertically */
  justify-content: flex-end; /* Aligns child to the right */
  margin: 20px;
  margin-bottom: 40px;
  height: 50px;
  width: 98%; /* Set width to 100% to take up the full width of the screen */
  @media (max-width: 750px) {
    flex-direction: column;
    height: auto;
    margin: 0px;
  }
`;

export const NavLinkA = styled(Link)`
  color: #ffffff;
  font-size: 20px;
  font-weight: bolder;
  text-decoration: none;
  @media (max-width: 1100px) {
    font-size: 16px; /* Set font size to 17px when screen size is less than 75% */
  }
`;

export const NavBarUl = styled.ul`
  height: 100%;
  background: #0d1b2a;
  border-radius: 25rem 0rem 0rem 25rem;
  list-style: none;
  display: flex;
  align-items: center;
  justify-content: space-evenly;
  flex-grow: 1;
  margin-top: 0;
  @media (max-width: 750px) {
    flex-direction: column;
    border-radius: 0rem;
    height: auto;
    min-height: 60px;
  }
`;

export const NavBarButton = styled.button`
  width: 150px;
  height: relative;
  background: #0d1b2a;
  border: none;
  border-radius: 0rem 52rem 52rem 0rem;
  color: #ffffff;
  font-size: 20px;
  font-weight: 800;
  margin-left: 15px;
  display: flex; /* Use flexbox for alignment */
  align-items: center; /* Center items vertically */
  justify-content: center; /* Center items horizontally */
  text-align: center; /* Center text */
  @media (max-width: 1100px) {
    font-size: 16px; /* Set font size to 17px when screen size is less than 75% */
  }
  @media (max-width: 750px) {
    width: 100%;
    border-radius: 0rem;
    margin-left: 0rem;
    height: 40px;
    // display:none;
    display: ${({ isVisible }) =>
      isVisible ? "flex" : "none"}; /* Conditional display */
  }
`;

export const NavBarLi = styled.li`
  align-items: center;
  @media (max-width: 750px) {
    margin: 1rem;
    // display:none;
    display: ${({ isVisible }) =>
      isVisible ? "flex" : "none"}; /* Conditional display */
  }
`;

export const MobileMenuDiv = styled.div`
  position: absolute;
  flex-direction: column;
  justify-content: space-between;
  width: 2.25rem;
  height: 2rem;
  top: 1rem;
  right: 1rem;
  @media (max-width: 750px) {
    display: flex;
  }
`;

export const MobileMenuSpan = styled.span`
  height: 0.4rem;
  width: 100%;
  background-color: #ffffff;
  border-radius: 0.2rem;
`;
