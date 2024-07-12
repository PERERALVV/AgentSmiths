import React, { useEffect, useState } from "react";
import SupportBot from "../components/pages/Support/supportbot";
import FaqItem from "../components/pages/Support/FaqItem";
import ChatbotButton from "../components/pages/Support/chatbotButton";
import styled from "styled-components";
import io from "socket.io-client";

const backend = "http://localhost:8080/";
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
      <SupportPageBody>
        <FAQlist>
          {FAQs.map((faq, index) => (
            <FaqItem key={index} Question={faq.question} Answer={faq.answer} />
          ))}
        </FAQlist>
        <SupportLeftContainer>
          <div style={{ display: isActive ? "block" : "none" }}>
            <div style={{ display: "flex", justifyContent: "flex-end" }}>
              <SupportBot setActive={setActive} socket={socket} close={close} />
            </div>
          </div>
          <div
            style={{
              display: isActive ? "none" : "flex",
              flexDirection: isActive ? "none" : "column",
            }}
          >
            <Simg></Simg>
            <div style={{ display: "flex", justifyContent: "flex-end" }}>
              <ChatbotButton setActive={setActive} open={open} />
            </div>
          </div>
        </SupportLeftContainer>
      </SupportPageBody>
    </SupportPageContainer>
  );
};

const SupportPageContainer = styled.div`
  display: flex;
  width: 100vw;
  justify-content: center;
  flex-direction: column;
`;

const SupportPageBody = styled.div`
  display: flex;
  flex-direction: column;
  gap: 12px;
  justify-content: center;
  margin: 2%;
  @media (min-width: 1100px) {
    flex-direction: row;
  }
`;

const SupportLeftContainer = styled.div`
  flex-shrink: 0;
  display: flex;
  justify-content: flex-right;
  gap: 12px;
  flex-direction: column;
  margin-top: 2%;
  margin-bottom: 2%;
  overflow-y: auto;
  overflow-x: hidden;
  position: sticky;
  top: 0;
  @media (max-width: 768px) {
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

const Simg = styled.div`
  width: 500px;
  height: 500px;
  background: url("./images/FAQs.gif");
  @media (max-width: 1100px) {
    display: none;
  }
`;
export default SupportPage;
