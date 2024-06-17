import React,{useEffect, useState} from "react";
import io from 'socket.io-client';
import Message from "./Message";

import '../../styles/components/Chat.css';
import SendIcon from '@mui/icons-material/Send';
import { GradientTextDiv } from "../../styles/components/GradientText";

const socket = io('http://localhost:8000',{
    path:'/sockets', //Not api??
});

function Chat() {
    const [isConnected, setIsConnected] = useState(socket.connected);
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');
    const [responses, setResponses] = useState([]);

    useEffect(()=>{
        socket.on('connect',() => {
            setIsConnected(socket.connected);
            console.log('Socket connected');
        });

        socket.on('disconnect',() => {
            setIsConnected(socket.connected);
            console.log('Socket disconnected');
        });

        socket.on('join',(data) => {
            setMessages((prevMessages)=>[...prevMessages,{...data,type:'join'}]);
            console.log('Joined:', data);
        })

        socket.on('chat',(data) => {
            setMessages((prevMessages)=>[...prevMessages,{...data,type:'chat'}]);
            console.log('Received chat message:', data);
        })

        socket.on('chat_response', (data) => {
            setResponses((prevResponses) => [...prevResponses, { ...data, type: 'chat_response' }]);
            console.log('Received chat response:', data);
        });

    },[]);
    console.log('Rendered with messages:', messages);
    console.log('Rendered with responses:', responses);
    return (
        <>
            <GradientTextDiv>{isConnected?'Connected':'Disconnected'}</GradientTextDiv>
            <div className="custom-scrollbar">
                {messages.map((message,index)=>(
                    // <Message message={message} key={index}/>
                    <div className="mx-3"key={index}>
                        <Message content={messages[index]} />
                        {/* {responses.filter(response => response.sid === message.sid).map((response, index) => (
                            <Message content={response}/>
                        ))} */}
                        {responses[index] && <Message content={responses[index]} />}
                        {/* HERE THE MESSAGE IS DISPLAYED AFTER THE ANSWER. FIX THIS ISSUE USING THE METHOD SUGGESTED BY CHATGPT
                        IT INVOLVES PARING MESSAGES AND RESPONSES. SINCE WE WANT TO PAIR LLM QUESTIONS AND ANSWERS AND NOT THE RESPONCE AND NEXT QUESTION, 
                        I'M NOT GOING TO FIX THAT HERE YET */}
                    </div>
                ))}
            </div>
            <hr className="w-60 mx-auto text-muted"/>
            <div className="SendMessage">
                {/* MAKE THIS RESPONSIVE ALONG WITH THE MAIN DIV */}                
                <input 
                    className="Input-Field"
                    placeholder="Type your message..."
                    type={'text'} 
                    id='message' 
                    onChange={(event)=>{
                        const value = event.target.value.trim();
                        setMessage(value);
                    }}
                ></input>
                <button 
                    className="GetStarted"
                    onClick={()=>{
                    if(message && message.length){
                        socket.emit('chat',message);
                    }
                    var messageBox = document.getElementById('message');
                    messageBox.value='';
                    setMessage('');

                }}>
                    <SendIcon className="Send-Icon"/>
                </button>  
            </div>
        </>
    );
  }

export default Chat;