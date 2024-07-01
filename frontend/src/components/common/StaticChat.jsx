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
        const { value, checked } = e.target;

        setResponses(prevResponses => {
            const currentAnswer = prevResponses[questionId]?.answers || '';
    
            let newValue;
            if (optionType === 'checkbox') {
                const currentChecks = Array.isArray(currentAnswer) ? currentAnswer : [];
                newValue = checked
                    ? [...currentChecks, value]
                    : currentChecks.filter(item => item !== value);
            } else {
                newValue = value;
            }
    
            return {
                ...prevResponses,
                [questionId]: {
                    questionId: questionId,
                    question: questionsAnswers.find(q => q.id === questionId).question,
                    answers: newValue,
                },
            };
        });
    };

    const handleSubmit = (questionId) => {

        // Ensure all questions have been answered
        const allQuestionsAnswered = questionsAnswers.every(q => responses[q.id]?.answers);

        // Mark question as submitted
        setSubmittedQuestions(prevState => [...prevState, questionId]);

        // Clear the current response
        setCurrentResponse({});

        if (Object.keys(responses).length + 1 === questionsAnswers.length) {
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
                                        checked={responses[questionAnswer.id]?.answers === option}
                                        disabled={submittedQuestions.includes(questionAnswer.id)}
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
                                        checked={responses[questionAnswer.id]?.answers?.includes(option)}
                                        disabled={submittedQuestions.includes(questionAnswer.id)}
                                    />
                                    <label htmlFor={`checkbox-${index}-${idx}`}>{option}</label>
                                </div>
                            ))}
                            {questionAnswer.answer_type === 'text' && (
                                <input 
                                    type="text" 
                                    name={`question-${index}`} 
                                    placeholder="Your answer here" 
                                    value={responses[questionAnswer.id]?.answers || ''}
                                    onChange={(e) => handleChange(e, questionAnswer.id, 'text')}
                                    disabled={submittedQuestions.includes(questionAnswer.id)}
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
        </ChatDiv>
    );
  }

export default StaticChat;



