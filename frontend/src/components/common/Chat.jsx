import React,{useEffect, useState} from "react";
import io from 'socket.io-client';
import Message from "./Message";
import { IoSendSharp } from "react-icons/io5";
import { GradientTextDiv } from "../../styles/components/GradientText";
import { ChatDiv, ChatHr, ChatScrollDiv, ClarifyButton, MessageContainerDiv, ReqChatButton, ReqChatInputDiv, ReqChatInputField } from "../../styles/components/ChatBox";
import { useNavigate } from 'react-router-dom';
// import { ToastContainer, toast } from 'react-toastify';
// import 'react-toastify/dist/ReactToastify.css';

const socket = io('http://localhost:80', { transports: ['websocket'] });  // Use only WebSocket to prevent fallback transport issues

function Chat() {
    const navigate = useNavigate();

    const [isConnected, setIsConnected] = useState(socket.connected);
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');
    const [sid, setSid] = useState('');  
    const [warningTimer, setWarningTimer] = useState(null);
    const [navigateTimer, setNavigateTimer] = useState(null);
    const [isInputDisabled, setIsInputDisabled] = useState(false);
    const [warningCount, setWarningCount] = useState(0); 
    // const [responses, setResponses] = useState([]);

    useEffect(()=>{
        const handleConnect = () => {
            setIsConnected(true);
            setSid(socket.id);  // Capture the socket ID
            console.log('Socket connected');
            socket.emit('start_conversation')
        };

        const handleDisconnect = () => {
            setIsConnected(false);
            console.log('Socket disconnected');
        };

        const handleStartConversation = () => {
            console.log('handleStartConversation');
        };

        const handleChatResponse = (data) => {
            setMessages((prevMessages) => [...prevMessages, { ...data, type: 'chat_response' }]);
            console.log('Received chat response:', data);
            setIsInputDisabled(false);
            startInactivityTimers();
        };

        const handleWarning = (data) => {
            setMessages((prevMessages) => [...prevMessages, { ...data, type: 'warning' }]);
            console.log('Received warning from backend:', data);

            setWarningCount((prevCount) => {
                const newCount = prevCount + 1;
                if (newCount >= 3) {
                    // toast.error('Your session will be terminated in 2 seconds.');
                    setTimeout(() => {
                        navigate('/'); 
                    }, 5000);  
                }
                return newCount;
            });

            setIsInputDisabled(false);
            startInactivityTimers();
        };

        const handleEndConversation = () => {
            console.log('Starting to create the website');
            socket.emit('end_conversation');
        }

        socket.on('connect', handleConnect);
        socket.on('disconnect', handleDisconnect);
        socket.on('chat_response', handleChatResponse);
        socket.on('warning', handleWarning);
        socket.on('end_conversation', handleEndConversation);
        socket.on('start_conversation', handleStartConversation);

        // Cleanup to avoid multiple listeners
        return () => {
            socket.off('connect', handleConnect);
            socket.off('disconnect', handleDisconnect);
            socket.off('chat_response', handleChatResponse);
            socket.off('warning', handleWarning);
            socket.off('end_conversation', handleEndConversation);
            socket.off('start_conversation', handleStartConversation);
        };
    },[]); 

    const handleMessageSend = () => {
        if (message.trim()) {
            setMessages((prevMessages) => [...prevMessages, { sid: sid, message: message.trim(), type: 'chat' }]);
            socket.emit('chat', message);
            var messageBox = document.getElementById('message');
            messageBox.value='';	            
            setMessage('');  
            setIsInputDisabled(true);

            // Clear any existing inactivity timers
            clearTimeout(warningTimer);
            clearTimeout(navigateTimer);
        }
    };

    const handleHelpAnswer = () => {
        // Find the last 'chat_response' message
        const lastChatResponse = [...messages].reverse().find(msg => msg.type === 'chat_response');
        console.log('Help request for:', lastChatResponse);
        if (lastChatResponse) {
            socket.emit('help_answer', lastChatResponse.message);
            setIsInputDisabled(true);
            console.log('Sent help request for:', lastChatResponse.message);
        } else {
            console.warn('No chat_response message found.');
        }
    };

    const startInactivityTimers = () => {
        // Clear any existing timers
        clearTimeout(warningTimer);
        clearTimeout(navigateTimer);

        // Set a timer for the warning message
        const newWarningTimer = setTimeout(() => {
            setMessages((prevMessages) => [
                ...prevMessages,
                { sid: sid, message: 'You have not responded for 120 seconds. Please respond to avoid conversation termination', type: 'warning' }
            ]);
            console.warn('User inactivity warning sent.');

            // Set a timer to navigate to home after another 2 minutes
            const newNavigateTimer = setTimeout(() => {
                navigate('/');
                console.warn('User redirected to HomePage due to inactivity.');
            }, 120000); // 2 minutes

            setNavigateTimer(newNavigateTimer);
        }, 120000); // 2 minutes

        setWarningTimer(newWarningTimer);
    };

    console.log('Rendered with messages:', messages);

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
                <ReqChatButton onClick={handleMessageSend} disabled={isInputDisabled}>
                    <IoSendSharp size={25} color={'#07297A'}/>
                </ReqChatButton>  
            </ReqChatInputDiv>
            <ClarifyButton onClick={handleHelpAnswer} disabled={isInputDisabled}>Help me answer</ClarifyButton>
        </ChatDiv>
    );
  }

export default Chat;



