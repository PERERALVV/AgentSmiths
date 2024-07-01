import React,{useEffect, useState} from "react";
// import io from 'socket.io-client';
import Message from "./Message";
import { IoSendSharp } from "react-icons/io5";
import { GradientTextDiv } from "../../styles/components/GradientText";
import { ChatDiv, ChatHr, ChatScrollDiv, StaticMessageContainerDiv, ReqChatButton, ReqChatInputDiv, ReqChatInputField, MessageContainerDiv } from "../../styles/components/ChatBox";
import { useNavigate, useSubmit } from 'react-router-dom';

// const socket = io('http://localhost:80', { transports: ['websocket'] });  // Use only WebSocket to prevent fallback transport issues

function StaticChat() {
    const navigate = useNavigate();
    const [isConnected, setIsConnected] = useState(true); // Assume connected as there's no backend in this context
    const [questionsAnswers, setQuestionsAnswers] = useState([]);
    const [responses, setResponses] = useState([]);
    const [currentResponse, setCurrentResponse] = useState({});
    const [submittedQuestions, setSubmittedQuestions] = useState([]);
    // const [sid, setSid] = useState('');  
    const userSid = 'user123'; //TEMP!!!!!!!!!!!!!!!!!!//////////////////
    // const [messages, setMessages] = useState([]);
    // const [message, setMessage] = useState('');
    // const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);

    useEffect(()=>{
        // Fetch questions from static_questions.json in public folder
        const fetchQuestions = async () => {
            try {
                const response = await fetch('/static_questions.json');
                const data = await response.json();
                setQuestionsAnswers(data);
                console.log(data)
            } catch (error) {
                console.error('Error fetching questions and answers:', error);
            }
        };

        fetchQuestions();
    },[]); 

    const handleChange = (e, questionId, optionType) => {
        const { name, value, checked } = e.target;

        setCurrentResponse(prevState => {
            let newValue;
            if (optionType === 'checkbox') {
                // Handle checkbox input
                const currentChecks = prevState.answers || [];
                newValue = checked
                    ? [...currentChecks, value]
                    : currentChecks.filter(item => item !== value);
            } else {
                // Handle radio button or text input
                newValue = value;
            }

            return {
                ...prevState,
                questionId: questionId,
                question: questionsAnswers.find(q => q.id === questionId).question,
                answers: newValue,
            };
        });
    };

    const handleSubmit = (questionId) => {
        setResponses(prevResponses => {
            // Check if the question has already been answered
            const existingResponseIndex = prevResponses.findIndex(r => r.questionId === questionId);
            if (existingResponseIndex !== -1) {
                // Update existing response
                const updatedResponses = [...prevResponses];
                updatedResponses[existingResponseIndex] = currentResponse;
                return updatedResponses;
            } else {
                // Add new response
                return [...prevResponses, currentResponse];
            }
        });

        // Mark question as submitted
        setSubmittedQuestions(prevState => [...prevState, questionId]);

        // Clear the current response
        // setCurrentResponse({});

        // Check if all questions have been answered
        if (responses.length + 1 === questionsAnswers.length) {
            console.log('All responses:', responses);
            navigate('/DemoPage');
        }
    };

    return (
        <ChatDiv>
            <GradientTextDiv>{isConnected?'You are connected':'Disconnected'}</GradientTextDiv>
            <ChatScrollDiv>
{/* ========================================================================== */}
            <MessageContainerDiv>
            {questionsAnswers.map((questionAnswer, index) => (
                        // <Message key={index} content={msg.message} />
                    <StaticMessageContainerDiv key={index}>
                        <div>
                            {questionAnswer.question}
                        </div>
                        <div>
                            {questionAnswer.answer_type === 'radio_button' && questionAnswer.options.map((option, idx) => (
                                <div key={idx}>
                                    <input 
                                        type="radio" 
                                        id={`radio-${index}-${idx}`} 
                                        name={`question-${index}`} 
                                        value={option} 
                                        onChange={(e) => handleChange(e, questionAnswer.id, 'radio_button')}
                                        checked={currentResponse.answers === option}
                                    />
                                    <label htmlFor={`radio-${index}-${idx}`}>{option}</label>
                                </div>
                            ))}
                            {questionAnswer.answer_type === 'checkbox' && questionAnswer.options.map((option, idx) => (
                                <div key={idx}>
                                    <input 
                                        type="checkbox" 
                                        id={`checkbox-${index}-${idx}`} 
                                        name={`question-${index}`} 
                                        value={option} 
                                        onChange={(e) => handleChange(e, questionAnswer.id, 'checkbox')}
                                        checked={currentResponse.answers?.includes(option)}
                                    />
                                    <label htmlFor={`checkbox-${index}-${idx}`}>{option}</label>
                                </div>
                            ))}
                            {questionAnswer.answer_type === 'text' && (
                                <input 
                                    type="text" 
                                    name={`question-${index}`} 
                                    placeholder="Your answer here" 
                                    value={currentResponse.answers || ''}
                                    onChange={(e) => handleChange(e, questionAnswer.id, 'text')}
                                />
                            )}
                        </div>
                        {!submittedQuestions.includes(questionAnswer.id) && (
                            <button type="button" onClick={() => handleSubmit(questionAnswer.id)}>Submit</button>
                        )}
                        {/* <button type="button" onClick={() => handleSubmit(questionAnswer.id)}>Submit</button> */}
                    </StaticMessageContainerDiv>
            ))}
            </MessageContainerDiv>
{/* ========================================================================== */}
            </ChatScrollDiv>
            {/* <ChatHr/>
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
            </ReqChatInputDiv> */}
        </ChatDiv>
    );
  }

export default StaticChat;



