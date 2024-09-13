import React from "react";
import styled from "styled-components";

const Actions = ({ fetch_chatlist, markAsDone, review }) => {
  return (
    <AcContainer>
      <ActionHeading>Chat Actions</ActionHeading>
      <ActionButton onClick={fetch_chatlist}>
        <ActionText>refresh chat list</ActionText>
      </ActionButton>
      <ActionButton onClick={markAsDone}>
        <ActionText>mark as done</ActionText>
      </ActionButton>
      <ActionButton onClick={review}>
        <ActionText>mark for review</ActionText>
      </ActionButton>
    </AcContainer>
  );
};

const AcContainer = styled.div`
  border-radius: 25px;
  background: #d9d9d9;
  width: 258px;
  height: 567px;
  flex-shrink: 0;
  padding: 10px;
  display: flex;
  flex-direction: column;
  gap: 50px;
  align-items: center;
`;
const ActionHeading = styled.h1`
  color: #000;
  text-align: center;
  font-family: "tahoma";
  font-size: 25px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  width: 250px;
  height: 38px;
  flex-shrink: 0;
`;
const ActionButton = styled.button`
  all: unset; // This removes all default styles
  cursor: pointer; // This changes the cursor to a pointer when hovering over the button
  border-radius: 25px;
  background: #0d1b2a;
  width: 230px;
  height: 58px;
  flex-shrink: 0;
  &:active {
    // This applies styles when the button is clicked
    box-shadow: 0 10px 10px #999; // This adds a glow effect
  }
`;

const ActionText = styled.h1`
  color: #fff;
  text-align: center;
  font-family: "tahoma";
  font-size: 20px;
  font-style: normal;
  font-weight: 700;
  line-height: normal;
  width: 230px;
`;
export default Actions;
