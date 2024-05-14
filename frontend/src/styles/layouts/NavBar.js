import styled from "styled-components";

export const NavBarDiv = styled.div`
    display:flex;
    // align-items: center; /* Center-align items vertically */
    // padding: 2rem;
    margin:20px;
    margin-bottom:40px;
    height : 50px;
    width: 100%; /* Set width to 100% to take up the full width of the screen */
    @media (max-width: 800px) {
      display: none; /* Hides the container when screen size is less than 700px */
  }
`;

export const NavLinkA = styled.a`
    color:#ffffff;
    font-size: 20px;
    font-weight: bolder;
    text-decoration: none;
    @media (max-width: 1100px) {
      font-size: 16px; /* Set font size to 17px when screen size is less than 75% */
  }
`;

export const NavBarUl = styled.ul`
  list-style: none;
  display: flex;
  border-radius: 25px 0px 0px 25px;
  background: #0D1B2A;
  align-items: center; 
  height: 100%;
  justify-content: space-evenly; 
  flex-grow: 1;
`;

export const NavBarButton = styled.button`
  width: 150px;
  height: relative;
  background: #0D1B2A;
  border: none;
  border-radius:  0px 52px 52px 0px;
  color: #ffffff;
  font-size: 20px;
  font-weight: 800;
  margin-left: 15px;
  // margin-bottom: 0;
  @media (max-width: 1100px) {
    font-size: 16px; /* Set font size to 17px when screen size is less than 75% */
}
`;

export const NavBarLi = styled.li`
  align-items: center; 
`;

export const NavBarLiHover = styled(NavBarLi)`
  &:hover {
    background: #ffffff;;
  }
`;