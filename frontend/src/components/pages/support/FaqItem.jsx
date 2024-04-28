import styled from "styled-components";

const FaqItemChild = styled.div`
  width: 1163px;
  height: 204px;
  position: relative;
  border-radius: var(--br-6xl);
  background-color: var(--color-gainsboro);
  display: none;
  max-width: 100%;
`;
const Question = styled.h3`
  margin: 0;
  position: relative;
  font-size: inherit;
  font-weight: 600;
  font-family: inherit;
  display: inline-block;
  max-width: 100%;
  z-index: 1;
  @media screen and (max-width: 825px) {
    font-size: var(--font-size-10xl);
  }
  @media screen and (max-width: 450px) {
    font-size: var(--font-size-3xl);
  }
`;
const Answer = styled.div`
  height: 83px;
  width: 1033px;
  position: relative;
  display: inline-block;
  flex-shrink: 0;
  mix-blend-mode: normal;
  max-width: 100%;
  z-index: 1;
  @media screen and (max-width: 450px) {
    font-size: var(--font-size-xl);
  }
`;
const AnswerWrapper = styled.div`
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-end;
  max-width: 100%;
  font-size: var(--font-size-6xl);
  color: var(--color-black);
  font-family: var(--font-inter);
`;
const FaqItemRoot = styled.div`
  align-self: stretch;
  border-radius: var(--br-6xl);
  background-color: var(--color-gainsboro);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-10xl) var(--padding-10xl) var(--padding-7xl)
    var(--padding-12xl);
  box-sizing: border-box;
  gap: var(--gap-mid);
  max-width: 100%;
  text-align: left;
  font-size: var(--font-size-17xl);
  color: var(--color-gray-200);
  font-family: var(--font-open-sans);
`;

const FaqItem = () => {
  return (
    <FaqItemRoot>
      <FaqItemChild />
      <Question>Can I alter my website whenever I want?</Question>
      <AnswerWrapper>
        <Answer>of course silly you can !!!!!!!</Answer>
      </AnswerWrapper>
    </FaqItemRoot>
  );
};

export default FaqItem;
