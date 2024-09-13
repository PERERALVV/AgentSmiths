import styled from "styled-components";

export const HomeDiv = styled.div``;

export const HomePage = styled.div`
  width: 98%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-content: flex-start;
  // gap: 10px;
  margin: 20px;
`;

export const HomePageContentBG = styled.div`
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  margin: 0%;
`;

export const HomePageDescription = styled.div`
  width: auto;
  height: 500px;
  word-wrap: "break-word";
  text-align: justify;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  @media (max-width: 800px) {
    width: 100%; /* Hides the container when screen size is less than 700px */
    margin-right: 30px;
  }
`;

export const HomePageIntroImage = styled.div`
  width: 100%;
  height: 100%;
  margin: 1rem;
  @media (max-width: 800px) {
    display: none;
  }
`;

export const HomePageImage = styled.img`
  width: 100%;
  height: 100%;
  align-content: center;
  margin: 0;
  padding: 0;
`;
