import React,{useEffect, useState} from "react";
import io from 'socket.io-client';
import Message from "./Message";
import { IoSendSharp } from "react-icons/io5";
import { GradientTextDiv } from "../../styles/components/GradientText";
import { ChatDiv, ChatHr, ChatScrollDiv, MessageContainerDiv, ReqChatButton, ReqChatInputDiv, ReqChatInputField } from "../../styles/components/ChatBox";

const socket = io('http://localhost:80', { transports: ['websocket'] });  // Use only WebSocket to prevent fallback transport issues
// const socket = io('http://localhost:80');

function Chat() {
    const [isConnected, setIsConnected] = useState(socket.connected);
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');
    // const [responses, setResponses] = useState([]);

    useEffect(()=>{
        const handleConnect = () => {
            setIsConnected(true);
            console.log('Socket connected');
        };

        const handleDisconnect = () => {
            setIsConnected(false);
            console.log('Socket disconnected');
        };

        const handleJoin = (data) => {
            setMessages((prevMessages) => [...prevMessages, { ...data, type: 'join' }]);
            console.log('Joined:', data);
        };

        const handleChatResponse = (data) => {
            setMessages((prevMessages) => [...prevMessages, { ...data, type: 'chat_response' }]);
            console.log('Received chat response:', data);
        };

        socket.on('connect', handleConnect);
        socket.on('disconnect', handleDisconnect);
        socket.on('join', handleJoin);
        socket.on('chat_response', handleChatResponse);

        // Cleanup to avoid multiple listeners
        return () => {
            socket.off('connect', handleConnect);
            socket.off('disconnect', handleDisconnect);
            socket.off('join', handleJoin);
            socket.off('chat_response', handleChatResponse);
        };
    },[]); 

    const handleMessageSend = () => {
        if (message.trim()) {
            setMessages((prevMessages) => [...prevMessages, { message: message.trim(), type: 'chat' }]);
            socket.emit('chat', message);
            setMessage('');  // Clear message after sending
        }
    };

    console.log('Rendered with messages:', messages);
    // console.log('Rendered with responses:', responses);
    return (
        <ChatDiv>
            <GradientTextDiv>{isConnected?'You are connected':'Disconnected'}</GradientTextDiv>
            <ChatScrollDiv>
{/* ========================================================================== */}
            <MessageContainerDiv>
            {messages.map((message,index)=>(
                // <Message key={index} content={messages[index]} />
                <Message key={index} content={messages[index]} />
            ))}
            </MessageContainerDiv>
{/* ========================================================================== */}
            </ChatScrollDiv>
            <ChatHr/>
            <ReqChatInputDiv>            
                <ReqChatInputField 
                    className="Input-Field"
                    placeholder="Type your message..."
                    type={'text'} 
                    id='message' 
                    onChange={(event)=>{
                        const value = event.target.value.trim();
                        setMessage(value);
                    }}
                ></ReqChatInputField >
                <ReqChatButton 
                    className="GetStarted"
                    onClick={handleMessageSend}>
                    <IoSendSharp size={25} color={'#07297A'}/>
                </ReqChatButton>  
            </ReqChatInputDiv>
        </ChatDiv>
    );
  }

export default Chat;



