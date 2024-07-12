import { Link } from "react-router-dom";
import styled from "styled-components";

export const NavBarDiv = styled.nav`
  display: flex;
  // align-items: center; /* Center-align items vertically */
  justify-content: flex-end;
  margin: 20px;
  margin-bottom: 40px;
  height: 50px;
  width: 98%;
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
    font-size: 16px;
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
  margin-top: 0px;
  @media (max-width: 750px) {
    flex-direction: column;
    border-radius: 0rem;
    height: auto;
    min-height: 60px;
    width: 100%;
  }
`;

export const NavBarButton = styled.button`
  width: 150px;
  height: relative;
  background: #0d1b2a;
  border: none;
  border-radius: 0rem 52rem 52rem 0rem;
  color: #ffffff;
  font-size: 24px;
  font-weight: Bold;
  font-family: "Nunito", sans-serif;
  margin-left: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  @media (max-width: 1100px) {
    font-size: 16px;
  }
  @media (max-width: 750px) {
    width: 108%;
    border-radius: 0rem;
    margin: 0px;
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
