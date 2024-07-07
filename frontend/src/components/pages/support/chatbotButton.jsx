import React from 'react';
import Button from '@mui/material/Button';
import styled from 'styled-components';
import {StyledEngineProvider} from '@mui/material/styles';
import { darken } from '@mui/system';

const ChatbotButton = ({setActive,  open}) => {
const handleClick=()=>{
  setActive(1)
  open()
}
return (
    <StyledEngineProvider injectFirst>
    <StyledButton variant="contained" endIcon={<ChatbotAvatar src="/images/bot.png" />} onClick={handleClick} >
        <Styledtext>Hey I’m here to help</Styledtext>
    </StyledButton>
    </StyledEngineProvider>
);
}


const StyledButton = styled(Button)`
  width: 472px;
  height: 136px;
  flex-shrink: 0;
  border-radius: 50px 50px 0px 50px;
  background: #D9D9D9;
  &:hover {
    background: ${darken('#D9D9D9', 0.1)};
  }
`;
const ChatbotAvatar = styled.img`
width: 85px;
height: 85px;
flex-shrink: 0;
border-radius: 100px;
background: url(<path-to-image>) lightgray 50% / cover no-repeat;
`;
const Styledtext=styled.span`
width: 289px;
height: 98px;
flex-shrink: 0;
color: #0D1B2A;
font-family: "Open Sans";
font-size: 36px;
font-style: normal;
font-weight: 700;
line-height: normal;
`;
export default ChatbotButton;