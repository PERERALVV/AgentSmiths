import { useState } from "react";
import React, { useEffect } from "react";
import io from "socket.io-client";
import "@chatscope/chat-ui-kit-styles/dist/default/styles.min.css";
import {
  MainContainer,
  ChatContainer,
  MessageList,
  Message,
  MessageInput,
  TypingIndicator,
} from "@chatscope/chat-ui-kit-react";
import {
  ChatbotRoot,
  ChatbotInner,
  ChatHeader,
  ChatbotChild,
  Download1Icon,
  Text1,
  Title,
  SupportingText,
  BlogSectionsavatarWithText,
  IconicActions,
  MoreOptionsIcon,
  CloseChatIcon,
} from "../../../styles/components/chatbot";

const backend = "http://127.0.0.1:8000";

const socket = io(backend);

const Chatbot = ({ setActive }) => {
  const [messages, setMessages] = useState([
    {
      message: "Hello, have a question about AgentSmiths? Ask me anything!",
      direction: "incoming",
      sender: "SupportBot",
    },
  ]);

  const [isTyping, setIsTyping] = useState(false);

  const handleSend = async (message) => {
    const newMessage = {
      message,
      direction: "outgoing",
      sender: "user",
    };

    const newMessages = [...messages, newMessage];

    setMessages(newMessages);

    setIsTyping(true);

    socket.emit("chat", message);
  };

  useEffect(() => {
    socket.on("response", (data) => {
      console.log(data);
      setMessages([
        ...messages,
        {
          message: data,
          direction: "incoming",
          sender: "SupportBot",
        },
      ]);
      setIsTyping(false);
    });
  });

  // Initialize chatbot when component mounts and disconnect when it unmounts
  React.useEffect(() => {
    socket.emit("init");

    // This function will be called when the component unmounts
    return () => {
      socket.emit("close");
    };
  }, []);
  return (
    <ChatbotRoot>
      <ChatbotChild />
      <ChatHeader>
        <BlogSectionsavatarWithText>
          <Download1Icon loading="lazy" alt="" src="/download-11@2x.png" />
          <Text1>
            <Title>Support Bot</Title>
            <SupportingText>Automated chat</SupportingText>
          </Text1>
        </BlogSectionsavatarWithText>
        <IconicActions>
          <MoreOptionsIcon alt="" src="/more-options.svg" />
          <button
            style={{
              border: "none",
              background: "none",
              padding: 0,
              margin: 0,
            }}
            onClick={() => setActive(0)}
          >
            <CloseChatIcon loading="lazy" alt="" src="/close-chat.svg" />
          </button>
        </IconicActions>
      </ChatHeader>
      <ChatbotInner>
        <ChatContainer style={{ maxHeight: "92.7%" }}>
          <MessageList
            scrollBehavior="auto"
            typingIndicator={
              isTyping ? <TypingIndicator content="I'm thinking...." /> : null
            }
            style={{
              backgroundColor: "var(--color-gainsboro)",
              minHeight: "100%",
              minWidth: "100%",
              padding: "0px 0px 0px 0px",
              fontSize: "(--font-size-6xl)",
              fontFamily: "var(--font-open-sans)",
              overflow: "auto",
            }}
          >
            {messages.map((message, i) => {
              console.log(message);
              return (
                <Message
                  key={i}
                  model={message}
                  style={{
                    alignContent: "end",
                    fontFamily: "var(--font-open-sans)",
                  }}
                />
              );
            })}
          </MessageList>
          <MessageInput
            style={{
              minWidth: "100%",
              backgroundColor: "var(--color-gainsboro)",
            }}
            placeholder="Type message here"
            onSend={handleSend}
          />
        </ChatContainer>
      </ChatbotInner>
    </ChatbotRoot>
  );
};

export default Chatbot;
