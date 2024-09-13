import React, { useEffect, useState } from "react";
// import FaqMenu from "../components/pages/Support/faqmenu";
import SupportBot from "../components/pages/Support/supportbot";
import FaqItem from "../components/pages/Support/FaqItem";
import ChatbotButton from "../components/pages/Support/chatbotButton";
import styled from "styled-components";
import io from "socket.io-client";

const backend = "http://localhost:8080/";
// const backend='http://127.0.0.1:8080/'
const socket = io(backend);
const close = () => {
  socket.emit("close");
  console.log("Chatbot disconnected");
};
const open = () => {
  socket.emit("init");
  console.log("Chatbot connected");
};
const SupportPage = () => {
  const [isActive, setActive] = useState(0);
  const [FAQs, setFAQs] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8080/faq");
        const data = await response.json();
        setFAQs(data);
        console.log(data);
      } catch (error) {
        console.error("Error fetching chat data:", error);
      }
    };
    fetchData();
    return close;
  }, []);
  return (
    <SupportPageContainer>
      <SupportPageHeader></SupportPageHeader>
      <SupportPageBody>
        <FAQlist>
          {/* <FaqItem></FaqItem>
          <FaqItem></FaqItem>
          <FaqItem></FaqItem>
          <FaqItem></FaqItem>
          <FaqItem></FaqItem>
          <FaqItem></FaqItem>
          <FaqItem></FaqItem> */}
          {FAQs.map((faq, index) => (
            <FaqItem
              key={index} // Add a unique key prop using the index
              Question={faq.question}
              Answer={faq.answer}
            />
          ))}
        </FAQlist>
        <SupportLeftContainer>
          <div style={{ display: isActive ? "block" : "none" }}>
            <SupportBot setActive={setActive} socket={socket} close={close} />
          </div>
          <div style={{ display: isActive ? "none" : "block" }}>
            {/* <FaqMenu /> */}
            <img src="./images/FAQs.gif" alt="" />
            <ChatbotButton setActive={setActive} open={open} />
          </div>
        </SupportLeftContainer>
      </SupportPageBody>
    </SupportPageContainer>
  );
};

const SupportPageContainer = styled.div`
  width: 98%;
`;
const SupportPageHeader = styled.span`
  width: 100%;
  height: 67px;
`;

const SupportPageBody = styled.span`
  display: flex;
  width: 100%;
  min-width: 1805px;
  min-height: 916px;
  flex-direction: row;
  gap: 12.814px;
  align-items: top;
  justify-content: center;
  margin: 2%;
  //   background: var(--bg-cool, red);

  @media (max-width: 768px) {
    flex-direction: column;
  }
`;

const SupportLeftContainer = styled.div`
  width: 527px;
  min-height: 916px;
  height: 100%;
  flex-shrink: 0;
  display: flex;
  gap: 12.814px;
  flex-direction: column;
  margin-top: 2%;
  margin-bottom: 2%;
  overflow-y: auto;
  overflow-x: hidden;
  position: sticky;
  top: 0;

  @media (max-width: 768px) {
    width: 100%;
    height: auto;
    justify-content: center;
    align-items: top;
  }
`;

const FAQlist = styled.div`
  display: flex;
  flex-direction: column;
  gap: 12.814px;
  margin-top: 2%;
  margin-bottom: 2%;
`;
export default SupportPage;
