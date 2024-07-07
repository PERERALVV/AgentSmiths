import React, { useEffect, useState } from "react";
import Chat from "../components/pages/supportAgent/chat";
import Actions from "../components/pages/supportAgent/quickActions";
import ChatList from "../components/pages/supportAgent/ConvoList";
import styled from "styled-components";
import io from "socket.io-client";

const backend = "http://localhost:8080/";
// const backend='http://127.0.0.1:8080'
const socket = io(backend);
const human_id = "vibuda";

const SupportAgentPage = () => {
  const [Chats, setChats] = useState([]);
  const [currentUser, setCurrentUser] = useState("");
  const [CurrentChat, setCurrentChat] = useState([]);
  const [currentchatlength, setCurrentChatLength] = useState(0);
  const [currentChatDone, setCurrentChatDone] = useState(true);
  const fetchData = async () => {
    try {
      const response = await fetch("http://localhost:8080/chatlist");
      const data = await response.json();
      setChats(data);
      console.log(data);

      // Check if currentUser exists in the fetched chats
      // const currentUserChat = data.find(chat => chat.user_id === currentUser);
      // if (!currentUserChat) {
      //   setCurrentChat([]);
      //   setCurrentChatLength(0);
      // }
    } catch (error) {
      console.error("Error fetching chat data:", error);
    }
  };
  const markAsDone = async () => {
    setCurrentChatDone(true);
    setCurrentChat([]);
    setCurrentChatLength(0);
    socket.emit("chat_Finished");
    fetchData();
  };
  const markForReview = async () => {
    const url = "http://localhost:8080/reviewChat"; // Example URL, adjust as needed
    const filteredChat = CurrentChat.filter(
      (chat) =>
        chat.hasOwnProperty("message") &&
        chat.message != null &&
        chat.message !== ""
    );
    console.log(filteredChat);
    const requestOptions = {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(filteredChat), // Send the filtered chat
    };
    try {
      // console.log(requestOptions.body);
      const response = await fetch(url, requestOptions);
      if (!response.ok) {
        // Handle non-200 responses
        throw new Error("Network response was not ok");
      }
      // Optionally, process the response data
      const data = await response.json();
      console.log(data); // Log or handle the response data as needed

      // Mark the chat as done after successful submission
      markAsDone();
    } catch (error) {
      console.error("Error submitting chat for review:", error);
    }
  };
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("http://localhost:8080/chatlist");
        const data = await response.json();
        setChats(data);
        console.log(data);
      } catch (error) {
        console.error("Error fetching chat data:", error);
      }
    };
    // Prompt for confirmation on page refresh
    fetchData();

    window.addEventListener("beforeunload", (event) => {
      event.preventDefault();
      event.stopPropagation();
      // event.returnValue = 'Are you sure you want to leave? All current chat sessions will be lost.';
    });

    // if you want to fetch regularly
    // const interval=setInterval(fetchData,10000)
    // return ()=>{
    //   clearInterval(interval)
    // }

    socket.emit("init_human", human_id);

    // Clean up on component unmount
    return () => {
      window.removeEventListener("beforeunload", (event) => {
        event.preventDefault();
        // event.returnValue = 'Are you sure you want to leave? All current chat sessions will be lost.';
      });
      socket.emit("close_human", human_id);
    };
  }, []);

  const onChatSelect = (user_id) => {
    // console.log(user_id);
    const chat = Chats.find((chat) => chat.user_id === user_id);
    console.log(chat);
    if (chat) {
      const updatedChats = Chats.filter((chat) => chat.user_id !== user_id);
      setChats(updatedChats);
      console.log("sent");
      socket.emit("human_accept", { user_id: user_id, human_id: human_id });
      socket.on("connection_result_to_human", (data) => {
        console.log(data);
        if (data === "connected") {
          setCurrentChat(chat.messages);
          setCurrentChatLength(chat.messages.length);
          console.log(chat.messages.length);
          setCurrentUser(user_id);
          const updatedChats = Chats.filter((chat) => chat.user_id !== user_id);
          setChats(updatedChats);
          setCurrentChatDone(false);
          console.log("Connection with user established");
        } else if (data === "error") {
          alert("User no longer available");
        }
      });
    }
  };

  useEffect(() => {
    socket.on("chat_from_bot", (data) => {
      if (data.user_id !== currentUser) {
        const chat = Chats.find((chat) => chat.user_id === data.user_id);

        if (chat) {
          const newMessage = {
            message: data.message,
            direction: "incoming",
            sender: "SupportBot",
          };

          chat.messages.push(newMessage);
        }
      }
    });
  });

  return (
    <SupportAgentPageContainer>
      <SupportAgentPageHeader></SupportAgentPageHeader>
      <SupportAgentPageBody>
        <PageChatQContainer>
          <ChatList
            chats={Chats}
            onChatSelect={onChatSelect}
            noOngoingChat={currentChatDone}
          />
        </PageChatQContainer>
        <PageActionsConytainer>
          <Actions
            fetch_chatlist={fetchData}
            markAsDone={markAsDone}
            review={markForReview}
          />
        </PageActionsConytainer>
        <PagechatContainer>
          <Chat
            messages={CurrentChat}
            user_id={currentUser}
            socket={socket}
            setMessages={setCurrentChat}
            chatlength={currentchatlength}
          />
        </PagechatContainer>
      </SupportAgentPageBody>
    </SupportAgentPageContainer>
  );
};
const SupportAgentPageContainer = styled.div`
  width: 45%;
`;
const SupportAgentPageHeader = styled.span`
  width: 100%;
  height: 67px;
`;

const SupportAgentPageBody = styled.span`
  width: 100%;
  height: auto;
  display: flex;
  flex-direction: row;
  gap: 100px;
  margin-left: 2%;
  margin-right: 2%;

  @media (max-width: 768px) {
    flex-direction: column;
    align-items: center;
  }
`;

const PagechatContainer = styled.div`
  width: 100%;
  max-width: 533px;
  height: auto;
  flex-shrink: 0;
`;

const PageActionsConytainer = styled.div`
  width: 100%;
  max-width: 258px;
  height: auto;
  flex-shrink: 0;
`;

const PageChatQContainer = styled.div`
  width: 100%;
  max-width: 890px;
  height: auto;
  flex-shrink: 0;
`;

export default SupportAgentPage;
