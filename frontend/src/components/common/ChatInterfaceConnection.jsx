import React, {useState, useEffect} from "react";
import io from "socket.io-client";
import '../../styles/components/ChatInterfaceConnection.css';
import SendIcon from '@mui/icons-material/Send';

let endPoint = "http://localhost:5000";
let socket = io.connect(`${endPoint}`);

const ChatInterfaceConnection = () => {
  const [messages, setMessages] = useState(["Hello and Welcome"]);
  const [message, setMessage] = useState([""]);

  useEffect(()=>{
    getMessages();
  },[messages.length]);

  const getMessages = () => {
    socket.on("message", msg =>{
      setMessages([...messages, msg]);
    });
  };

  const onChange = e => {
    setMessage(e.target.value);
  };

  const onClick = () => {
    if (message !== ""){
      socket.emit("message",message);
      setMessage("");
    }else{
      alert("Please Add A Message");
    }
  };

  return(
    <div>
      {messages.length > 0 && messages.map((msg, index) => (
        <div key={index} className="ChatMessagesContainer">
          <p className="ChatMessages">{msg}</p>
          {/* <p>{index}</p> */}
        </div>
      ))
      }

        <div className="SendMessage">
            <input type="text" className="Input-Field" value={message} name="message" onChange={e=>onChange(e)} placeholder="Type your website's domain..."/>
            <button className="GetStarted" type="submit" onClick={() => onClick()}><SendIcon className="Send-Icon"/></button>
        </div>

    </div>
  );

};

export default ChatInterfaceConnection;
