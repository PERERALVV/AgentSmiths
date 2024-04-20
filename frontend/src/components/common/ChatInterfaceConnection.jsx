import React, { useState, useEffect } from "react";
import '../../styles/components/ChatInterfaceConnection.css';
import SendIcon from '@mui/icons-material/Send';

const ChatInterfaceConnection = () => {
  const [messages, setMessages] = useState(["Hello and Welcome"]);
  const [message, setMessage] = useState("");
  const [socket, setSocket] = useState(null); // Add state for the WebSocket connection

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:8000/ws"); // Connect to your backend WebSocket endpoint
    setSocket(ws); // Store the WebSocket connection in state
  
    ws.onmessage = event => {
      console.log("Received message from server:", event.data);
      const data = event.data.split(":"); // Split received data into type and message
      const messageType = data[0];
      const messageContent = data[1];
      
      // Check message type
      if (messageType === "backend") {
        // Update messages based on previous state
        console.log("Updating messages with content:", messageContent);
        setMessages(prevMessages => [...prevMessages, messageContent]);
      }
    };
    

  // Cleanup function to close WebSocket connection
  return () => {
    if (ws) {
      ws.close();
    }
  };
  }, []); // Empty dependency array ensures this effect runs only once on component mount

  const onChange = e => {
    setMessage(e.target.value);
  };

  const onClick = () => {
    if (message !== "") {
      // Send message to server with message type and client ID
      if (socket) {
        const clientID = "chatInterface"; // Client ID for chatInterface
        const messageWithPrefix = `${clientID}:${message}`;
        console.log("Sending message to server:", messageWithPrefix);
        socket.send(messageWithPrefix);
      }
      setMessage("");
    } else {
      alert("Please Add A Message");
    }
  };    

  return (
    <div>
      {messages.map((msg, index) => (
        <div key={index} className="ChatMessagesContainer">
          <p className="ChatMessages">{msg}</p>
        </div>
      ))}
      <div className="SendMessage">
        <input
          type="text"
          className="Input-Field"
          value={message}
          name="message"
          onChange={onChange}
          placeholder="Type your message..."
        />
        <button className="GetStarted" type="submit" onClick={onClick}>
          <SendIcon className="Send-Icon"/>
        </button>
      </div>
    </div>
  );
};

export default ChatInterfaceConnection;
