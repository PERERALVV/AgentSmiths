import styled from "styled-components";

export const ChatInterfaceDiv = styled.div`
  // text-align: center;
  display: flex;
  flex-direction: row;
  width: 98%;
  height: 100vh;
  padding: 2rem;
  padding-right: 0rem;
  background: #ffffff;
  // gap: 30px;
`;

export const LeftHolderDiv = styled.div`
  width: 20%;
  height: 100%;
  max-height: 100%;
  @media (max-width: 900px) {
    display: none;
  }
`;

export const LeftHolderImage = styled.img`
  max-width: 100%;
  max-height: 50%;
  width: auto;
  height: auto;
  margin-top: 100px;
  margin-botton: 0px;
`;

export const RightHolderDiv = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #e0e4f7;
  border: none;
  border-right: 0px;
  border-radius: 20px;
  padding: 1rem;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); /* Box shadow */
  width: 30%;
  max-height: 100%;
  border-radius: 20px 0px 0px 20px;
  @media (max-width: 600px) {
    display: none;
  }
`;

export const RightHolderImage = styled.img`
  // max-width: 100%;
  // max-height: 50%;
  width: 50%;
  height: auto;
  align-self: center;
  margin-top: 100px;
  margin-botton: 0px;
`;

export const MiddleHolderDiv = styled.div`
  flex: 2;
  background-color: rgb(144, 166, 218, 0.5);
  border-radius: 2rem;
  padding: 10px;
  box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25);
  width: 700px;
  max-height: 100%;
  margin: 0 2rem;
  flex-shrink: 0;
`;

export const DownloadButton = styled.button`
  background-color: #07297a; /* Example button color */
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 0.5rem;
  cursor: pointer;
  font-size: 1rem;
  margin-top: 1rem;

  &:hover {
    background-color: #05468a; /* Darken on hover */
  }
`;
