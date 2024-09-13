import styled from "styled-components";

export const ChatDiv = styled.div`
    display: flex;
    flex-direction: column;
    width: 100%;
    height: 100%;
    align-items: center; /* Center items vertically */
    justify-content: center; /* Center items horizontally */
    // border-radius:2rem;
`;

export const ChatHr = styled.hr`
    width: 90%; /* Set the width to 60% */
    margin: 10px;
    border: 0; 
    border-top: 2px solid #6c757d;
`;

export const ChatScrollDiv = styled.div`
    height: 81%;
    width: 100%;
    overflow-y: scroll;

    &::-webkit-scrollbar {
        width: 12px; 
    }

    &::-webkit-scrollbar-track {
        background: transparent; /* Background of scrollbar track */
    }

    &::-webkit-scrollbar-thumb {
        background-color: #ffffff;
        border-radius: 6px; 
        border: 3px solid transparent; 
    }

    &::-webkit-scrollbar-thumb:hover {
        background-color: rgb(144, 166, 218); 
    }
`;

export const MessageContainerDiv = styled.div`
    margin: 1rem;
`;

export const ReqChatInputDiv = styled.div`
    display: flex;
    width: 100%;
    height: 40px;
    border-radius:2rem;
    // overflow: hidden;
`;

export const ReqChatInputField = styled.input`
    flex-grow:1;
    width: 100%;
    height: 100%;
    padding: 0 1rem;
    border: 0;
    border-radius:2rem 0rem 0rem 2rem;
    box-sizing: border-box; 
    &::placeholder{
      color: #797e79; 
      font-size: 16px;
    }
    @media (max-width: 1100px) {
        &::placeholder{
            font-size: 14px;
        }
    }
`;

export const ReqChatButton = styled.button`
    width: 80px;
    display: flex; 
    align-items: center; /* Center items vertically */
    justify-content: center; /* Center items horizontally */
    text-align: center; /* Center text */
    border:0px;
    border-radius: 0rem 2rem 2rem 0rem;
    background-color:  #ffffff;   
    font-weight: 400;
    flex-shrik: 5;
    @media (max-width: 1100px) {
        font-size: 14px;
    }
`;

export const ClarifyButton = styled.button`
    flex-grow:1;
    width: 50%;
    // height: 100%;
    padding: 0.25rem;
    margin: 0.5rem;
    border: 0;
    border-radius:2rem;
    box-sizing: border-box; 
    background-color:#07297A;
    color: #ffffff; 
    font-size: 14px;
    @media (max-width: 1100px) {
        &::placeholder{
            font-size: 12px;
        }
    }
`;



  
  