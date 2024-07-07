import {
  MessageList,
  Message,
  TypingIndicator,
  MessageSeparator,
} from "@chatscope/chat-ui-kit-react";
import styled from "styled-components";
import React, { useState, useEffect } from "react";
// import SendIcon from '@mui/icons-material/Send';
// import IconButton from "@mui/material/IconButton";
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";

import ChatbotInput from "../../common/chatbotInput";

const Chat = ({ messages, user_id, socket, setMessages, chatlength }) => {
  console.log(chatlength);
  const human_id = "vibuda";

  const [isTyping, setIsTyping] = useState(false);
  const purifyText = (htmlString) => {
    // Create a new DOMParser instance
    const parser = new DOMParser();
    // Parse the input string as HTML
    const doc = parser.parseFromString(htmlString, "text/html");
    // Extract and return the text content, stripping out HTML tags
    return doc.body.textContent || "";
  };
  const handleSend = async (message) => {
    message = purifyText(message);

    const newMessage = {
      message,
      direction: "outgoing",
      sender: "user",
    };

    const newMessages = [...messages, newMessage];

    setMessages(newMessages);

    setIsTyping(true);
    // the human id here should be replaced by the support agent id
    socket.emit("chat_from_human", { human_id: human_id, data: message });
  };

  useEffect(() => {
    if (chatlength === 0) {
      setIsTyping(false);
    }
  }, [chatlength]);
  // Initialize chatbot when component mounts and disconnect when it unmounts
  // useEffect(() => {
  //   socket.emit('init_human',human_id);

  //   // This function will be called when the component unmounts
  //   return () => {
  //     socket.emit('close_human',human_id);
  //   };
  // }, []);

  useEffect(() => {
    socket.on("chat_from_bot", (data) => {
      if (data.user_id === user_id) {
        console.log(data);
        setMessages([
          ...messages,
          {
            message: data.data,
            direction: "incoming",
            sender: "SupportBot",
          },
        ]);
        setIsTyping(false);
      }
    });
  });
  return (
    <Container>
      <StyledHeader>
        <StyledFlexDiv>
          <SupportBotImg src="/images/bot.png" alt="" />
          <StyledH1>SupportBot</StyledH1>
        </StyledFlexDiv>
      </StyledHeader>
      <MessageList
        style={{
          width: "528px",
          height: "604px",
          flexShrink: 0,
          background: "rgba(217, 217, 217, 0.00)",
        }}
        scrollBehavior="auto"
        typingIndicator={
          isTyping ? (
            <TypingIndicator content="waiting for user reply...." />
          ) : null
        }
      >
        {/* make the rest referiing the oldchatbot in myvm/supportpage */}

        {/* {chat.map((message, i) => (
                <Message 
                  key={i} 
                  model={message} 
                  style={{
                    // borderRadius: '15px',
                    // background: '#FFF',
                    // width: '263.293px',
                    // height: '56.25px',
                    // flexShrink: 0
                  }}
                />
            ))} */}
        {messages.map((message, i) =>
          i === chatlength - 1 ? (
            <>
              <Message key={i} model={message} style={{}} />
              <MessageSeparator
                as="h1"
                content="chat with human starts from here"
              />
            </>
          ) : (
            <>
              <Message key={i} model={message} style={{}} />
            </>
          )
        )}
      </MessageList>
      <ChatbotInput handleSend={handleSend} />
    </Container>
  );
};

const Container = styled.div`
  border-radius: 25px 25px 0px 25px;
  background: #d9d9d9;
  width: 533px;
  // height: 837px;
  flex-shrink: 0;
  outline: 2px solid #000;
`;
const StyledHeader = styled.div`
  display: flex;
  width: 533px;
  height: 111px;
  padding: 17.085px;
  align-items: center;
  flex-shrink: 0;
  border-radius: 25.628px 25.628px 0px 0px;
  background: var(--bg-cool, #f9f9fb);
`;
const StyledFlexDiv = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 12.814px;
  flex: 1 0 0;
`;
const StyledH1 = styled.h1`
  width: 329px;
  color: #000;
  text-align: center;
  font-family: "Open Sans";
  font-size: 25px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
`;
const SupportBotImg = styled.img`
  width: 50px;
  height: 50px;
  border-radius: 100px;
  background: url(<path-to-image>) lightgray 50% / cover no-repeat;
`;

// const StyledMessageList = styled.div`
// width: 528px;
// height: 604px;
// flex-shrink: 0;
// background: rgba(217, 217, 217, 0.00);
// `;

// const StyledsendButtonConainer = styled.div`
// display: flex;
// width: 76.884px;
// height: 76.884px;
// justify-content: center;
// align-items: center;
// gap: 12.814px;
// flex-shrink: 0;
// `;

// const StyledsendButton = styled(IconButton)`
// display: flex;
// padding: 4.271px;
// justify-content: center;
// align-items: center;
// border-radius: 17.085px;
// `;
// const StyledsendIcon = styled(SendIcon)`
// width: 25.628px;
// height: 25.628px;
// `;
export default Chat;
