import React,{useEffect, useState} from "react";
import io from 'socket.io-client';
import { GradientTextDiv } from "../../styles/components/GradientText";
import { ChatDiv, ChatScrollDiv, MessageContainerDiv } from "../../styles/components/ChatBox";
import { useNavigate, useSubmit } from 'react-router-dom';
import { OptionContainerDiv, OptionDiv, QuestionContainerDiv, SubmitButton, StaticMessageContainerDiv, DescriptionTextArea,  } from "../../styles/pages/StaticChat";

const socket = io('http://localhost:80', { transports: ['websocket'] }); 

function StaticChat() {
    const navigate = useNavigate();
    const [isConnected, setIsConnected] = useState(socket.connected); 
    const [questionsAnswers, setQuestionsAnswers] = useState([]);
    const [responses, setResponses] = useState([]);
    const [currentResponse, setCurrentResponse] = useState({});
    const [submittedQuestions, setSubmittedQuestions] = useState([]);
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [sessionid, setSid] = useState('');  
    const [pageDescriptions, setPageDescriptions] = useState([]);

    useEffect(()=>{

        const handleConnect = () => {
            setIsConnected(true);
            setSid(socket.id);  
            console.log('Socket connected');
        };

        const handleDisconnect = () => {
            setIsConnected(false);
            console.log('Socket disconnected');
        };

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
                
        socket.on('connect', handleConnect);
        socket.on('disconnect', handleDisconnect);

        fetchQuestions();

        return () => {
            socket.off('connect', handleConnect);
            socket.off('disconnect', handleDisconnect);
        };
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
                    label: questionsAnswers.find(q => q.id === questionId).label,
                    answers: newValue,
                },
            };
        });
    };

    const handleSubmit = (questionId) => {

        const allQuestionsAnswered = questionsAnswers.every(q => responses[q.id]?.answers);

        setSubmittedQuestions(prevState => [...prevState, questionId]);
        
        setCurrentResponse({});

        setCurrentQuestionIndex(prevIndex => {
            if (prevIndex + 1 < questionsAnswers.length) {
                return prevIndex + 1;
            } else {
                if (allQuestionsAnswered && currentQuestionIndex === questionsAnswers.length - 1) {
                    console.log('All responses:', responses);
                }
                return prevIndex;
            }
        });
    };

    const handleDescriptionChange = (e, pageName) => {
        // Debugging: Check form target
        console.log('Form target:', e.target);
        const { value } = e.target;
        console.log(value);
    
        setPageDescriptions(prevDescriptions => {
            // Update the specific description for the given pageName
            const updatedDescriptions = prevDescriptions.map(desc =>
                desc.pageName === pageName ? { ...desc, description: value } : desc
            );
    
            // If pageName does not exist, add a new entry
            if (!updatedDescriptions.find(desc => desc.pageName === pageName)) {
                updatedDescriptions.push({ pageName, description: value });
            }
    
            return updatedDescriptions;
        });
    };    

    const handleSubmitPageDescriptions = (e) => {
        e.preventDefault();
    
        // Create descriptions from pageDescriptions state
        const descriptions = pageDescriptions.map(desc => ({
            pageName: desc.pageName,
            description: desc.description,
        }));
    
        console.log('Page Descriptions:', descriptions);
    
        // Create the conversation data
        const conversation = Object.values(responses).map(response => ({
            // questionId: response.questionId,
            // question: response.question,
            label: response.label,
            answers: response.answers,
        }));
    
        socket.emit('static_chat', sessionid, sessionid, conversation, descriptions);
        navigate('/Demo');
    };

    return (
        <ChatDiv>
            <GradientTextDiv>{isConnected?'You are connected':'Disconnected'}</GradientTextDiv>
            <ChatScrollDiv>
            <MessageContainerDiv>
            {questionsAnswers.slice(0, currentQuestionIndex + 1).map((questionAnswer, index) => (
                        // <Message key={index} content={msg.message} />
                    <StaticMessageContainerDiv key={index}>
                        <QuestionContainerDiv>
                            {questionAnswer.question}
                        </QuestionContainerDiv>
                        <OptionContainerDiv>
                            {questionAnswer.answer_type === 'radio_button' && questionAnswer.options.map((option, idx) => (
                                <OptionDiv key={idx}>
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
                                </OptionDiv>
                            ))}
                            {questionAnswer.answer_type === 'checkbox' && questionAnswer.options.map((option, idx) => (
                                <OptionDiv key={idx}>
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
                                </OptionDiv>
                            ))}
                            {questionAnswer.answer_type === 'text' && (
                                <DescriptionTextArea 
                                    name={`question-${index}`} 
                                    placeholder="Your answer here" 
                                    value={responses[questionAnswer.id]?.answers || ''}
                                    onChange={(e) => handleChange(e, questionAnswer.id, 'text')}
                                    disabled={submittedQuestions.includes(questionAnswer.id)}
                                />
                            )}
                        </OptionContainerDiv>
                        {!submittedQuestions.includes(questionAnswer.id) && (
                            <SubmitButton type="button" onClick={() => handleSubmit(questionAnswer.id)}>Submit</SubmitButton>
                        )}
                    </StaticMessageContainerDiv>
            ))}
            {questionsAnswers.every(q => responses[q.id]?.answers) && (
            <StaticMessageContainerDiv>
                {responses[5]?.answers.map((answer,index)=>(
                    <div key={index}>
                        <QuestionContainerDiv>{answer}</QuestionContainerDiv>
                        <DescriptionTextArea  
                            name={`description-${answer}`} 
                            placeholder="Please provide a brief description about this web page" 
                            onChange={(e) => handleDescriptionChange(e, answer)}
                            value={pageDescriptions.find(desc => desc.pageName === answer)?.description || ''}
                        />
                    </div>
                ))}
                <SubmitButton type="submit" onClick={handleSubmitPageDescriptions}>Submit</SubmitButton>
            </StaticMessageContainerDiv>)}
            </MessageContainerDiv>
            </ChatScrollDiv>
        </ChatDiv>
    );
  }

export default StaticChat;



