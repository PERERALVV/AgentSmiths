import styled from "styled-components";

export const ChatInterfaceDiv = styled.div`
    // text-align: center;
    display: flex;
    flex-direction: row;   
    width: 100%;
    height: 100vh;
    padding: 2rem;  
    padding-right: 0rem;
    background: #ffffff;
    // gap: 30px;
`;

export const LeftHolderDiv = styled.div`
    width : 20%;
    height: 100%;
    max-height: 100%;
    @media (max-width: 900px) {
        display: none;
    }
`;

export const LeftHolderImage = styled.img`
    max-width: 100%;
    max-height: 50%;
    width: auto; /* Adjust to allow the image to maintain its aspect ratio */
    height: auto; /* Adjust to allow the image to maintain its aspect ratio */
    align-self: flex-end; /* Align the image to the bottom of the div */
    margin-top:100px;
    margin-botton:0px;
`;

export const RightHolderDiv = styled.div`
    flex: 1; /* Use flex-grow to make both holders take equal width */
    background-color: none; /* 50% transparent white background */
    border: 2px solid #3A40CB;
    border-right: 0px;
    border-radius: 20px; /* Rounded corners */
    padding: 1rem; /* Padding for inner content */
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); /* Box shadow */
    width : 30%;
    max-height: 100%;
    border-radius: 20px 0px 0px 20px;
    @media (max-width: 600px) {
        display: none;
    }
`;

export const MiddleHolderDiv = styled.div`
    flex: 2; 
    background-color: rgb(144, 166, 218, 0.5); 
    border-radius: 2rem; 
    padding: 10px; 
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); 
    width : 700px;
    max-height: 100%;
    margin : 0 2rem;
    flex-shrink: 0;
`;