import styled from "styled-components";

export const GetStartedInputDiv = styled.div`
  display: flex;
  width: 100%;
  height: 40px;
  border-radius: 2rem;
  // overflow: hidden;
`;

export const GetStartedInputField = styled.input`
  flex-grow: 1;
  height: 100%;
  padding: 0 1rem;
  border: 2px solid #0d1b2a;
  border-radius: 2rem 0 0 2rem;
  box-sizing: border-box;
  font-size: 16px;
  font-family: "Nunito", sans-serif;
  &::placeholder {
    color: #797e79;
    font-size: 16px;
    font-weight: 400;
  }
  @media (max-width: 1100px) {
    &::placeholder {
      font-size: 14px;
    }
  }
`;

export const GetStartedButton = styled.button`
  width: 200px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 0 1rem;
  border: 2px solid #0d1b2a;
  border-radius: 0rem 2rem 2rem 0rem;
  background-color: #0d1b2a;
  color: #ffffff;
  font-weight: 400;
  font-family: "Nunito", sans-serif;
  box-sizing: border-box;
  @media (max-width: 1100px) {
    font-size: 16px;
  }
`;
