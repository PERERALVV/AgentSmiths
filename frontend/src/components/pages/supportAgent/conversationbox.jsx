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
  background: #fff;
  width: 815px;
  height: 127.742px;
  flex-shrink: 0;
  padding: 20px;
  &:active {
    // This applies styles when the button is clicked
    box-shadow: 0 0 10px #999; // This adds a glow effect
  }
`;
const Conversationwrapper = styled.div`
  width: 815px;
  height: 141.34px;
  flex-shrink: 0;
`;
const Username = styled.h1`
  all: unset;
  width: 259px;
  height: 37.262px;
  flex-shrink: 0;
  color: #000;
  text-align: center;
  font-family: "tahoma";
  font-size: 25px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
`;

const Content = styled.p`
  color: #000;
  text-align: left;
  font-family: "tahoma";
  font-size: 25px;
  font-style: normal;
  font-weight: 400;
  line-height: normal;
  width: 800px;
  height: 74.525px;
  flex-shrink: 0;
`;

export default ConversationBox;
