import styled from 'styled-components';

const FaqItem= ({Question,Answer})=> {
    return (
        <FaqContainer>
        <StyledQuestion>{Question}</StyledQuestion>
        <StyledAnswer>{Answer}</StyledAnswer>
        </FaqContainer>
    );
    }

export default FaqItem;

const FaqContainer = styled.div`
  width: 1163px;
  min-height: 204px;
  flex-shrink: 0;
  border-radius: 25px;
  background: #E0E1DD;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
`;

const StyledQuestion=styled.h2`
color: #0D1B2A;
font-family: "Open Sans";
font-size: 36px;
font-style: normal;
font-weight: 600;
line-height: normal;
padding-left: 20px;
`;

const StyledAnswer=styled.p`
width: 1033px;
height: 83px;
flex-shrink: 0;
color: #000;
font-family: Inter;
font-size: 25px;
font-style: normal;
font-weight: 400;
line-height: normal;
padding-left: 40px;
`