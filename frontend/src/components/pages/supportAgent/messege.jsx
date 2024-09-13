import React from 'react';
import {Message,Avatar } from '@chatscope/chat-ui-kit-react';
import { Style } from '@mui/icons-material';


const ChatMessage = ({i,message}) => {

    return (
        <><Avatar src="/images/bot.png" />
        <StyledMessage
            key={i}
            model={{ message }} /></>
    )
}

const StyledMessage= styled(Message)`
border-radius: 15px;
background: #FFF;
width: 263.293px;
height: 56.25px;
flex-shrink: 0;
`;