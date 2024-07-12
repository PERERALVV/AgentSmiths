import styled from "styled-components";

const FaqItem = ({ Question, Answer }) => {
  return (
    <FaqContainer>
      <StyledQuestion>{Question}</StyledQuestion>
      <StyledAnswer>{Answer}</StyledAnswer>
    </FaqContainer>
  );
};

export default FaqItem;

const FaqContainer = styled.div`
  max-width: 40vw;
  padding: 20px;
  border-radius: 25px;
  background: #e0e1dd;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  @media (max-width: 1100px) {
    max-width: 100vw;
  }
`;

const StyledQuestion = styled.div`
  color: #0d1b2a;
  font-family: "nunito";
  font-size: 36px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
  word-wrap: break-word;
  overflow-wrap: break-word;
`;

const StyledAnswer = styled.div`
  flex-shrink: 0;
  color: #000;
  font-family: "nunito";
  font-size: 25px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  word-wrap: break-word;
  overflow-wrap: break-word;
`;
