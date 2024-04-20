import React,{useEffect, useState} from "react";
import io from 'socket.io-client';
import Message from "./Message";

const socket = io('http://localhost:8000',{
    path:'/sockets',
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
            <h2>Status : {isConnected?'Connected':'Disconnected'}</h2>
            <div
                style={{
                    height:'500px',
                    overflowY:'scroll',
                    border:'solid black 1px',
                    padding:'10px',
                    marginTop:'15px',
                    display:'flex',
                    flexDirection:'column',
                }}
            >
                {messages.map((message,index)=>(
                    // <Message message={message} key={index}/>
                    <div key={index}>
                        <Message content={message} />
                        {/* {responses.filter(response => response.sid === message.sid).map((response, index) => (
                            <Message message={response} key={index} />
                        ))} */}
                    </div>
                ))}
                {responses.map((response,index)=>(
                    // <Message message={message} key={index}/>
                    <div key={index}>
                        <Message content={response} />
                        {/* {responses.filter(response => response.sid === message.sid).map((response, index) => (
                            <Message message={response} key={index} />
                        ))} */}
                    </div>
                ))}
            </div>
            <input 
                type={'text'} 
                id='message' 
                onChange={(event)=>{
                    const value = event.target.value.trim();
                    setMessage(value);
                }}
            ></input>
            <button onClick={()=>{
                if(message && message.length){
                    socket.emit('chat',message);
                }
                var messageBox = document.getElementById('message');
                messageBox.value='';
                setMessage('');

            }}>Send</button>
        </>
    );
  }

export default Chat;