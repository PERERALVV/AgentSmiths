import React,{useEffect, useState} from "react";
import io from 'socket.io-client';
import Message from "./Message";
import { IoSendSharp } from "react-icons/io5";
import { GradientTextDiv } from "../../styles/components/GradientText";
import { ChatDiv, ChatHr, ChatScrollDiv, MessageContainerDiv, ReqChatButton, ReqChatInputDiv, ReqChatInputField } from "../../styles/components/ChatBox";

const socket = io('http://localhost:80');

function Chat2() {
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
        <ChatDiv>
            {/* <GradientTextDiv>{isConnected?'Connected':'Disconnected'}</GradientTextDiv> */}
            <GradientTextDiv>{isConnected?'You are connected':'Disconnected'}</GradientTextDiv>
            <ChatScrollDiv>
                {messages.map((message,index)=>(
                    // <Message message={message} key={index}/>
                    <MessageContainerDiv key={index}>
                        <Message content={messages[index]} />
                        {responses[index] && <Message content={responses[index]} />}
                    </MessageContainerDiv>
                ))}
            </ChatScrollDiv>
            <ChatHr/>
            <ReqChatInputDiv>
                {/* MAKE THIS RESPONSIVE ALONG WITH THE MAIN DIV */}                
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
                    onClick={()=>{
                    if(message && message.trim().length > 0){
                        setMessages((prevMessages)=>[...prevMessages,{...message,type:'chat'}]);
                        socket.emit('chat',message);
                    }
                    var messageBox = document.getElementById('message');
                    messageBox.value='';
                    setMessage('');

                }}>
                    <IoSendSharp size={25} color={'#07297A'}/>
                </ReqChatButton>  
            </ReqChatInputDiv>
        </ChatDiv>
    );
  }

export default Chat2;