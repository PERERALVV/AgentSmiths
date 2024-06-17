import styled from "styled-components";

export const GetStartedInputDiv = styled.div`
    display: flex;
    width: 100%;
    height: 40px;
    border-radius:2rem;
`;

export const GetStartedInputField = styled.input`
    flex-grow:1;
    width: 100%;
    height: 100%;
    diplay: flex;
    align-items:start;
    flex-shrik: 5;
    border: 2px solid  #0D1B2A;
    border-radius:2rem 0rem 0rem 2rem;
    padding: 1rem;
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

export const GetStartedButton = styled.button`
    width: 200px;
    display: flex; /* Use flexbox for alignment */
    align-items: center; /* Center items vertically */
    justify-content: center; /* Center items horizontally */
    text-align: center; /* Center text */
    border:0px;
    border-radius: 0rem 2rem 2rem 0rem;
    background-color:  #0D1B2A;
    color:  #ffffff;    
    font-weight: 400;
    flex-shrik: 5;
    @media (max-width: 1100px) {
        font-size: 14px;
    }
`;

  
  