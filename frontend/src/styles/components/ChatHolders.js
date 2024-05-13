import styled from "styled-components";

export const LeftHolderDiv = styled.div`
    width : 20%;
    height: auto;
    min-height: 100vh;
    // background-color: bisque;
    justify-content: spece-between;
    @media (max-width: 700px) {
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

export const MiddleHolderDiv = styled.div`
    flex: 2; /* Use flex-grow to make both holders take equal width */
    background-color: rgba(151, 142, 142, 0.5); /* 50% transparent white background */
    // background: linear-gradient(to bottom, rgba(155, 155, 155, 0.23) 65px, rgba(151, 142, 142, 0.5) 40px); /* Pink color for top 40px */
    border-radius: 20px; /* Rounded corners */
    padding: 10px; /* Padding for inner content */
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); /* Box shadow */
    width : 700px;
    height: auto;
    min-height: 100vh;
    flex-shrink: 0;
`;

export const RightHolderDiv = styled.div`
    flex: 1; /* Use flex-grow to make both holders take equal width */
    background-color: none; /* 50% transparent white background */
    border: 2px solid #3A40CB;
    border-right: 0px;
    border-radius: 20px; /* Rounded corners */
    padding: 10px; /* Padding for inner content */
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); /* Box shadow */
    width : 30%;
    border-radius: 20px 0px 0px 20px;
    min-height: 100vh;
    // background-color: rgba(151, 142, 142, 0.5); /* 50% transparent white background */
`;

