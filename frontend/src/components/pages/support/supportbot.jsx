import React, { useState, useEffect } from 'react';
// import io from 'socket.io-client';
import Button from '@mui/material/Button';
import styled from 'styled-components';
import CloseIcon from '@mui/icons-material/Close';
import IconButton from "@mui/material/IconButton";

import { MessageList, Message,TypingIndicator,Avatar,Loader } from '@chatscope/chat-ui-kit-react';
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';

// import Button from '@material-ui/core/Button';
import ChatbotInput from '../../common/chatbotInput';




const SupportBot = ({setActive , close, socket}) => {

  const defaultMessages = [
    {
      message: "Hello, have a question about AgentSmiths? Ask me anything!",
      direction: 'incoming',
      sender: "SupportBot"
    }
  ];

  const [connected_with_human, setConnected_with_human] = useState(false);
  const [messages, setMessages] = useState(defaultMessages);
  const [waiting_for_human,setWaiting_for_human] = useState(false);
  const handleCloseClick = () => {
    setActive(0);
    close();
  !connected_with_human && setMessages(defaultMessages);
  }

  const [isTyping, setIsTyping] = useState(false);
  const purifyText=(htmlString) => {
    // Create a new DOMParser instance
    const parser = new DOMParser();
    // Parse the input string as HTML
    const doc = parser.parseFromString(htmlString, 'text/html');
    // Extract and return the text content, stripping out HTML tags
    return doc.body.textContent || "";
  }
  const handleSend = async (message) => {
    
    message=purifyText(message);
    
    const newMessage = {
      message,
      direction: 'outgoing',
      sender: "user"
    };

    const newMessages = [...messages, newMessage];
    
    setMessages(newMessages);

    setIsTyping(true);
    if (connected_with_human) {
      socket.emit('chat_to_human', message);
    } else {
      socket.emit('support/chat', message);
    }
  };

  const connectHuman = async () => {
    socket.emit('connect_to_human');
    close()
    setWaiting_for_human(true);
    socket.on('connection_result_to_user', (message) => {
      if (message === 'connected') {
        setConnected_with_human(true);
        setWaiting_for_human(false);
        console.log('Connected to human agent');
      }
    });
  }
  useEffect(() => {
    socket.on('response', (data) => {
      console.log(data);
      setMessages([...messages, {
        message: data,
        direction: 'incoming',
        sender: "SupportBot"
      }]);
      setIsTyping(false);
    });
    socket.on('chatFinished', () => {
      setConnected_with_human(false);
      
      const newMessages = [
        ...messages,
        {
          message: "Thank you for chatting with us.",
          direction: 'incoming',
          sender: "SupportBot"
        },
        {
          message: "your session has eneded and you are no longer connected",
          direction: 'incoming',
          sender: "SupportBot"
        },
        {
          message: "you may close this chat window now",
          direction: 'incoming',
          sender: "SupportBot"
        },
        {
          message: "if you nned to chat again please refresh the window",
          direction: 'incoming',
          sender: "SupportBot"
        },
      ];
      
      setMessages(newMessages);
      setIsTyping(false);
    });
  });

// Initialize chatbot when component mounts and disconnect when it unmounts
// useEffect(() => {
//   // This code runs when the component mounts
//   socket.emit('init');
//   console.log('Chatbot connected');

//   return () => {
//       // This code runs when the component unmounts
//       socket.emit('close');
//       console.log('Chatbot disconnected');
//     };
//   }, []); // Empty dependency array means this effect runs once on mount and cleanup on unmount
  return (
        <MContainer>
          <StyledHeader>
            <StyledFlexDiv>
              <SupportBotImg src="/images/bot.png" alt="" />
              <StyledH1>SupportBot</StyledH1>
            </StyledFlexDiv>
            <StyledclosebuttonWrapper>
            <ClosedButton onClick={handleCloseClick}><CloseIcon/></ClosedButton>
            </StyledclosebuttonWrapper>
          </StyledHeader> 
          <div style={{ position: 'relative' }}>
            <MessageList
              style={{
                width: '528px',
                height: '604px',
                flexShrink: 0,
                background: 'rgba(217, 217, 217, 0.00)'
              }}
              scrollBehavior="auto"
              typingIndicator={isTyping ? <TypingIndicator content={connected_with_human ? "waiting for human reply...." : "I'm thinking...."} /> : null}
            >
              {/* make the rest referring the old chatbot in myvm/supportpage */}
              {messages.map((message, i) => (
                message.direction === 'incoming' ? (
                  <Message 
                    key={i} 
                    model={message} 
                  >
                    <Avatar src="/images/bot.png" />
                  </Message>
                ) : (
                  <Message 
                    key={i} 
                    model={message} 
                  >
                  </Message>
                )
              ))}
            </MessageList>
            <div style={{
              display: waiting_for_human ? 'flex' : 'none',
              justifyContent: 'center',
              alignItems: 'center',
              position: 'absolute',
              top: 0,
              left: 0,
              width: '100%',
              height: '100%',
              backgroundColor: 'rgba(0,0,0,0.5)' // Adjust the background as needed
            }}>
              <Loader content="loading" />
            </div>
          </div>
          <HumanButtonFiller>
            <ConnectToHumanButton startIcon={<ConnectToHumanavatar src="/images/bothuman.png" alt="your agent pic" />} onClick={connectHuman}>
              <HumanButtonText>
              {connected_with_human ? "you are connected" : "connect with human agent"}
              </HumanButtonText>
            </ConnectToHumanButton>
          </HumanButtonFiller>
          <ChatbotInput handleSend={handleSend}/>
        </MContainer>
  )
}

const MContainer = styled.div`
  border-radius: 25px 25px 0px 25px;
  background: #D9D9D9;
  width: 527px;
  height: 914px;
  flex-shrink: 0;
  border: 1px solid black;
`;
const StyledHeader = styled.div`
  border-radius: 25.628px 25.628px 0px 0px;
  background: var(--bg-cool, #F9F9FB);
  display: flex;
  width: 493px;
  height: 111px;
  padding: 17.085px;
  align-items: center;
  flex-shrink: 0;
`;
const StyledFlexDiv = styled.div`
  display: flex;
  align-items: center;
  gap: 12.814px;
  flex: 1 0 0;
`;
const StyledH1 = styled.h1`
  display: flex;
  width: 157px;
  flex-direction: column;
  align-items: flex-start;
`;
const SupportBotImg = styled.img`
  border-radius: 100px;
  background: url(<path-to-image>) lightgray 50% / cover no-repeat;
  width: 50px;
  height: 50px;
`;
const ClosedButton = styled(IconButton)`
display: flex;
width: 42.714px;
height: 42.714px;
padding: 4.271px 4.271px 4.271px 4.272px;
justify-content: center;
align-items: center;
border-radius: 21.357px;
`;
const StyledclosebuttonWrapper = styled.div`
display: flex;
align-items: flex-start;
gap: 12.814px;
`;
const ConnectToHumanButton = styled(Button)`
width: 527px;
height: 68px;
flex-shrink: 0;
`;
const HumanButtonFiller = styled.div`
width: 527px;
height: 68px;
flex-shrink: 0;
border-radius: 50px 50px 0px 0px;
background: #0D1B2A;
`;
const HumanButtonText = styled.span`
display: flex;
width: 346.531px;
height: 37.053px;
flex-direction: column;
justify-content: center;
flex-shrink: 0;
backdrop-filter: blur(2px);
color: #FFF;
text-align: center;
-webkit-text-stroke-width: 1;
-webkit-text-stroke-color: #000;
font-family: Inter;
font-size: 25px;
font-style: normal;
font-weight: 600;
line-height: normal;
`;
const ConnectToHumanavatar = styled.img`
width: 49.646px;
height: 48px;
flex-shrink: 0;
border-radius: 60px 60px 0px 60px;
background: url(<path-to-image>) lightgray 50% / cover no-repeat;
`;
// const HumanButtoncontent = styled.div`
// width: 421px;
// height: 48px;
// flex-shrink: 0;
// `;
export default SupportBot;