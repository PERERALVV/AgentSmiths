import styled from "styled-components";

export const ShowOutputContainer = styled.div`
  display: flex;
  flex-direction: column;
  height: 100vh;
  width: 100vw;
`;
export const BottomBarContainer = styled.div`
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
  background-color: #444444;
`;

export const NavigationButton = styled.button`
  padding: 4px 0px;
  font-size: 16px;
  cursor: pointer;
  background-color: #dddddd;
  border-radius: 50px;
  border: none;
  display: flex;
  align-items: center;
  font-family: nunito;
  font-weight: bold;
  &:hover {
    background-color: #a0a0a0;
    transition: 0.1s;
  }
`;

export const ButtonImage = styled.img`
  width: 30px;
  height: 30px;
  margin: 0px 5px;
`;

export const CurrentFile = styled.div`
  font-size: 16px;
  margin: 0 20px;
  color: #dddddd;
  padding: 5px 10px;
  border-radius: 20px;
  font-weight: bold;
`;

export const RightDiv = styled.div`
  display: flex;
  gap: 40px;
`;

export const DownloadDiv = styled.div`
  width: 38px;
  height: 38px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  cursor: pointer;
`;
