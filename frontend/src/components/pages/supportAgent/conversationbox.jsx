import React from "react";
import styled from "styled-components";

const ConversationBox = ({ username, lastMessage, handleclick, disabled }) => {
  return (
    <Conversationwrapper>
      <StyledConversation
        onClick={() => !disabled && handleclick(username)}
        disabled={disabled} // Assuming 'disabled' is a state or prop that controls the disabled state
      >
        <Username>{username}</Username>
        <Content>{lastMessage}</Content>
      </StyledConversation>
    </Conversationwrapper>
  );
};
const StyledConversation = styled.button`
  all: unset; // This removes all default styles
  pointer-events: ${(props) => (props.disabled ? "none" : "auto")};
  opacity: ${(props) => (props.disabled ? 0.5 : 1)};
  cursor: pointer; // This changes the cursor to a pointer when hovering over the button
  border-radius: 25px;
  margin: 10px;
  width: 600px;
  background: #d9d9d9;
  // height: 127.742px;
  // flex-shrink: 0;
  padding: 20px;
  &:active {
    // This applies styles when the button is clicked
    box-shadow: 0 0 10px #999; // This adds a glow effect
  }
  @media (max-width: 768px) {
    max-width: 80vw;
  }
`;
const Conversationwrapper = styled.div`
  // width: 815px;
  // height: 141.34px;
  flex-shrink: 0;
`;
const Username = styled.div`
  all: unset;
  //width: 100%;
  //height: 205px;
  flex-shrink: 0;
  color: #000;
  text-align: left;
  font-family: "nunito";
  font-size: 25px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  word-wrap: break-word;
  overflow-wrap: break-word;
`;

const Content = styled.p`
  color: #000;
  text-align: left;
  font-family: "nunito";
  font-size: 25px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  //width: 100%;
  // height: 74.525px;
  flex-shrink: 0;
  word-wrap: break-word;
  overflow-wrap: break-word;
`;

export default ConversationBox;
