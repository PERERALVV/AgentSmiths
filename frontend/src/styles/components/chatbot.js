import styled from "styled-components";
import '@chatscope/chat-ui-kit-styles/dist/default/styles.min.css';
import { MainContainer, ChatContainer, MessageList, Message, MessageInput, TypingIndicator } from '@chatscope/chat-ui-kit-react';
export const ChatbotChild = styled.div`
  align-self: stretch;
  height: 837px;
  position: relative;
  border-radius: var(--br-6xl) var(--br-6xl) 0px var(--br-6xl);
  background-color: var(--color-gainsboro-100);
  display: none;
`;
export const Download1Icon = styled.img`
  height: 50px;
  width: 50px;
  position: relative;
  border-radius: var(--br-81xl);
  object-fit: cover;
`;
export const Title = styled.b`
  width: 121.2px;
  position: relative;
  display: inline-block;
`;
export const SupportingText = styled.div`
  align-self: stretch;
  position: relative;
  color: var(--grey-grey-300);
`;
export const Text1 = styled.div`
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px var(--padding-2xs) 0px 0px;
  box-sizing: border-box;
  min-width: 102px;
`;
export const BlogSectionsavatarWithText = styled.div`
  flex: 1;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  padding: 0px var(--padding-218xl) 0px 0px;
  box-sizing: border-box;
  gap: 12.814057350158691px;
  min-width: 207px;
  max-width: 100%;
  @media screen and (max-width: 450px) {
    flex-wrap: wrap;
    padding-right: var(--padding-99xl);
    box-sizing: border-box;
  }
`;
export const MoreOptionsIcon = styled.img`
  height: 42.7px;
  width: 42.7px;
  position: relative;
  border-radius: 21.36px;
  display: none;
  min-height: 43px;
`;
export const CloseChatIcon = styled.img`
  height: 42.7px;
  width: 42.7px;
  position: relative;
  border-radius: 21.36px;
`;
export const IconicActions = styled.div`
  height: 42.7px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 12.814058303833008px;
`;
export const ChatHeader = styled.div`
  align-self: stretch;
  border-radius: 25.63px 25.63px 0px 0px;
  background-color: var(--bg-cool);
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: flex-start;
  padding: var(--padding-11xl-5) 17.099999999998545px var(--padding-11xl-5)
    17.100000000000364px;
  box-sizing: border-box;
  max-width: 100%;
  row-gap: 20px;
  z-index: 1;
  @media screen and (max-width: 825px) {
    flex-wrap: wrap;
  }
`;


export const ChatbotInner = styled(MainContainer)`
  align-self: stretch;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 0px 0px 0px 0px;
  box-sizing: border-box;
  max-width: 100%;
  text-align: center;
  font-size: var(--font-size-sm);
  font-family: var(--font-inter);
  height: 100%;
`;
export const ChatbotRoot = styled.div`
  width: 533px;
  border-radius: var(--br-6xl) var(--br-6xl) 0px var(--br-6xl);
  background-color: var(--color-gainsboro-100);
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
  padding: 0px 0px var(--padding-base);
  box-sizing: border-box;
  height: 800px;
  // position: absolute; 
  bottom: 20px; 
  right: 20px; 
  min-width: 533px;
  max-width: 100%;
  text-align: left;
  font-size: var(--font-size-mid-1);
  color: var(--color-black);
  font-family: var(--font-open-sans);
  @media screen and (max-width: 1425px) {
    flex: 1;
  }
  @media screen and (max-width: 825px) {
    gap: 70px 141px;
    min-width: 100%;
  }
  @media screen and (max-width: 450px) {
    gap: 35px 141px;
  }
`;


