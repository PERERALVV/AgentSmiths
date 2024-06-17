import styled from "styled-components";

export const HomePage = styled.div`
    width: 100%; 
    height: 100%;
    display: flex;
    flex-direction: column;
    align-content: flex-start;
    gap: 100px;
    /* justify-content: space-evenly; */
    margin: 20px;
`;

export const HomePageContentBG = styled.div`
    width: 100%; 
    height: 100%;
    // background: rgba(3.90, 3.80, 3.80, 0.5);
    display: flex;
    align-items: center;
    /* justify-content: space-evenly; */
    margin: 0%;
`;

export const HomePageDescription = styled.div`
    width: 50%;
    height: 500px;
    color: #ffffff;
    font-weight: 800;
    word-wrap: 'break-word';
    text-align: justify;
    display: flex;
    flex-direction: column;
    justify-content: space-evenly;
    @media (max-width: 800px) {
        width:100%; /* Hides the container when screen size is less than 700px */
        margin-right: 30px;
    }
`;

export const HomePageIntroImage = styled.div`
width: auto;
height: 500px;
@media (max-width: 800px) {
    display: none; /* Hides the container when screen size is less than 700px */
}
`;

export const HomePageImage = styled.img`
    max-width: 100%;
    max-height: 100%;
    width:100%;
    height: 100%;
    align-content: center;
    margin: 0;
    padding: 0;
`;
  
  

  
  