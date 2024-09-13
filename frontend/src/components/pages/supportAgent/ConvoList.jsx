import React from "react";
import _ from "lodash";
import styled from "styled-components";
// import { ConversationList,Conversation } from '@chatscope/chat-ui-kit-react';
import ConversationBox from "./conversationbox";

const ChatList = ({ chats, onChatSelect, noOngoingChat }) => {
  const handleclick = (user_id) => {
    // console.log("clicked");
    // console.log(user_id);
    onChatSelect(user_id);
  };
  return (
    <StyledChatlist>
      {/* <ConversationBox></ConversationBox> */}
      {chats.map((chat, index) => {
        // Find the last message sent by the "User" starting from the end
        const lastUserMessage = _.findLast(
          chat.messages,
          (message) => message.sender === "User"
        );

        return (
          <div key={index}>
            <ConversationBox
              handleclick={handleclick}
              username={chat.user_id}
              lastMessage={
                lastUserMessage ? lastUserMessage.message : "No message"
              }
              disabled={!noOngoingChat}
            />
            <RowFlexDiv></RowFlexDiv>
          </div>
        );
      })}
    </StyledChatlist>
  );
};

const StyledChatlist = styled.div`
  width: 887px;
  height: 828px;
  flex-shrink: 0;
  background: #d9d9d9;
  padding: 20px;
  overflow: auto; // This makes the div scrollable

  /* Makes scrollbar invisible */
  ::-webkit-scrollbar {
    display: none;
  }
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
`;
const RowFlexDiv = styled.div`
  display: flex;
  flex-direction: row;
  height: 40px;
`;
export default ChatList;
