import React,{useEffect, useState} from "react";
import { useSocket } from '../../SocketContext';
// import io from 'socket.io-client';

import Message from "./Message";
import { IoSendSharp } from "react-icons/io5";
import { GradientTextDiv } from "../../styles/components/GradientText";
import { ChatDiv, ChatHr, ChatScrollDiv, ClarifyButton, MessageContainerDiv, ReqChatButton, ReqChatInputDiv, ReqChatInputField } from "../../styles/components/ChatBox";
import { useNavigate } from 'react-router-dom';

// const socket = io('http://localhost:80', { transports: ['websocket'] });  // Use only WebSocket to prevent fallback transport issues

function Chat() {
    const navigate = useNavigate();
    const { socket, sid } = useSocket();

    const [isConnected, setIsConnected] = useState(false);
    const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');
    // const [sid, setSid] = useState('');  
    const [warningTimer, setWarningTimer] = useState(null);
    const [navigateTimer, setNavigateTimer] = useState(null);
    const [isInputDisabled, setIsInputDisabled] = useState(false);
    const [warningCount, setWarningCount] = useState(0); 
    // const [responses, setResponses] = useState([]);

    useEffect(()=>{
        if (!socket) {
            console.warn("Socket is not available from the context.");
            return;
        }

        const handleConnect = () => {
            setIsConnected(true);
            // setSid(socket.id);  // Capture the socket ID
            console.log('Socket connected in Chat: ',sid);
            socket.emit('start_conversation')
        };

        const handleDisconnect = () => {
            setIsConnected(false);
            console.log('Socket disconnected in Chat');
        };

        const handleStartConversation = () => {
            console.log('handleStartConversation');
        };

        const handleMessageExchange = (data) => {
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

        const handleQnaWarning = (data) => {
            setMessages((prevMessages) => [...prevMessages, { ...data, type: 'warning' }]);
            console.log('Received qna warning from backend:', data);

            setIsInputDisabled(false);
            startInactivityTimers();
        };

        const handleEndConversation = () => {
            console.log('Starting to create the website');
            socket.emit('end_conversation');
            setMessages((prevMessages) => [
                ...prevMessages,
                { sid: sid, message: 'Yayy! Now I have all the information to create the perfect website for you! Your website is now being built.', type: 'chat_response' }
            ]);
            setIsInputDisabled(true);
        }

        const handleCodeReady = () => {
            console.log('Starting to create the website');
            //Show button
        }

        const handleSomethingWrong = () => {
            setMessages((prevMessages) => [
                ...prevMessages,
                { sid: sid, message: 'Oops! Something went wrong. You will be directed to the Home page', type: 'warning' }
            ]);
            console.warn('Something went wrong.');
            setTimeout(() => {
                navigate('/');
                console.warn('User redirected to HomePage due to inactivity.');
            }, 4000);
        }

        socket.on('connect', handleConnect);
        socket.on('disconnect', handleDisconnect);
        socket.on('message_exchange', handleMessageExchange);
        socket.on('warning', handleWarning);
        socket.on('qna_warning', handleQnaWarning);
        socket.on('start_conversation', handleStartConversation);
        socket.on('end_conversation', handleEndConversation);
        socket.on('code_ready',handleCodeReady);
        socket.on('something_wrong',handleSomethingWrong);

        // Cleanup to avoid multiple listeners
        return () => {
            socket.off('connect', handleConnect);
            socket.off('disconnect', handleDisconnect);
            socket.off('message_exchange', handleMessageExchange);
            socket.off('warning', handleWarning);
            socket.off('qna_warning', handleQnaWarning);
            socket.off('start_conversation', handleStartConversation);
            socket.off('end_conversation', handleEndConversation);
            socket.off('code_ready',handleCodeReady);
            socket.off('something_wrong',handleSomethingWrong);
        };
    },[socket]); 

    const handleMessageSend = () => {
        if (message.trim()) {
            setMessages((prevMessages) => [...prevMessages, { sid: sid, message: message.trim(), type: 'chat' }]);
            socket.emit('message_exchange', message);
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



