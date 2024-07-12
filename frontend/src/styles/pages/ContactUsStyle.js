import styled from "styled-components";

export const Container = styled.div`
  font-family: inherit;
  display: flex;
  min-height: 88vh;
  background-color: #ffffff;
  @media (max-width: 768px) {
    flex-direction: column;
  }
`;

export const ImageContainer = styled.div`
  max-height: 800px;
  flex: 1;
  background-image: url("./images/ContactUs.gif");
  background-size: cover;
  background-position: center;
  border-radius: 5px;
  @media (max-width: 768px) {
    display: none;
  }
`;

export const FormContainer = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  background-color: #f5f5f5;
  box-shadow: rgba(17, 17, 26, 0.1) 0px 1px 0px,
    rgba(17, 17, 26, 0.1) 0px 8px 24px, rgba(17, 17, 26, 0.1) 0px 16px 48px;
  border-radius: 5px;
  min-width: 560px;
`;

export const FormContent = styled.div`
  width: 100%;
  max-width: 500px;
`;

export const Header = styled.h1`
  margin-bottom: 20px;
  color: #333;
  font-size: 40px;
`;

export const SubHeader = styled.h2`
  margin-bottom: 10px;
  color: #666;
  font-size: 18px;
`;

export const CardsContainer = styled.div`
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-bottom: 20px;
  @media (max-width: 768px) {
    flex-direction: column;
  }
`;

export const StyledCard = styled.div`
  padding: 10px;
  margin: 5px;
  border: 1px solid ${(props) => (props.selected ? "#0d2b1a" : "#ccc")};
  border-radius: 30px;
  cursor: pointer;
  background: ${(props) => (props.selected ? "#0d2b1a" : "#f9f9f9")};
  color: ${(props) => (props.selected ? "#fff" : "#333")};
  transition: background 0.3s, border 0.3s, color 0.3s;
  &:hover {
    border: 1px solid #0d2b1a;
    background: #0d2b1a;
    color: #fff;
  }
  backdrop-filter: blur(5px);
  flex: 1 1 30%;
  text-align: center;
  @media (max-width: 768px) {
    flex: 1 1 100%;
  }
`;

export const Input = styled.input`
  width: 95%;
  padding: 12px;
  margin: 10px 0;
  border-radius: 30px;
  border: 1px solid #ccc;
  background: #f9f9f9;
  color: #333;
  font-size: 16px;
  transition: background 0.3s, border 0.3s, color 0.3s;
  &:hover {
    border: 1px solid #0d2b1a;
    background: #e0f2f1;
    color: #0d2b1a;
  }
  &:focus {
    border: 1px solid #0d2b1a;
    background: #e0f2f1;
    color: #0d2b1a;
    outline: none;
  }
`;

export const StyledButton = styled.button`
  display: flex;
  padding: 10px 20px;
  margin-top: 20px;
  border: none;
  border-radius: 30px;
  background-color: #0d2b1a;
  color: white;
  cursor: pointer;
  font-size: 16px;
  transition: background 0.3s;
  align-self: flex-end;
  &:hover {
    background-color: #000000;
  }
`;

export const CompanyDetails = styled.div`
  margin-top: 50px;
  color: #666;
  font-size: 14px;
`;

export const ToolbarContainer = styled.div`
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-around;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  background: #f9f9f9;
`;
