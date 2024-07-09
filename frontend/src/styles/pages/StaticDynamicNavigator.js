import styled from "styled-components";

export const MainContainer = styled.section`
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh);
  background: linear-gradient(180deg, #ffffff 0%, #a8a8a8 100%);
  @media (min-width: 750px) {
    flex-direction: row;
  }
`;

export const Card = styled.div`
  background: rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  margin: 20px;
  padding: 30px;
  width: 350px;
  height: 450px;
  text-align: center;
  color: #333;
  transition: transform 0.3s, box-shadow 0.3s;
  &:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  }
`;

export const CardTitle = styled.h2`
  font-size: 2rem;
  margin-bottom: 20px;
  background: linear-gradient(135deg, #007bff, #00b3ff);
  -webkit-background-clip: text;
  color: transparent;
`;

export const CardDetailsContainer = styled.div`
  height: 270px;
`;

export const CardDetails = styled.p`
  font-size: 1rem;
  margin-bottom: 30px;
  text-align: left;
`;

export const Button = styled.button`
  background: linear-gradient(135deg, #007bff, #00b3ff);
  border: none;
  border-radius: 50px;
  color: black;
  padding: 15px 30px;
  font-size: 1.2rem;
  font-weight: bold;
  font-family: "Nunito", sans-serif;
  cursor: pointer;
  transition: background 0.5s ease, transform 0.5s ease, box-shadow 0.5s ease;
  margin-top: 10px;
  box-shadow: 0 4px 15px rgba(0, 123, 255, 0.3);
  &:hover {
    background: linear-gradient(135deg, #00b3ff, #007bff);
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0, 123, 255, 0.5);
  }
  &:active {
    transform: translateY(1px);
    box-shadow: 0 4px 20px rgba(0, 123, 255, 0.4);
  }
`;
