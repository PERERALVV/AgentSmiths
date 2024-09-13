import React from 'react';
import { GetStartedButton, GetStartedInputDiv, GetStartedInputField } from '../../styles/components/InputFieldGetStarted';
import { useNavigate } from 'react-router-dom';

function InputFieldGetStarted() {
    const navigate = useNavigate();
    const handleGetStarted = () => {
      navigate('/GetStarted');
    };
    return (
        <GetStartedInputDiv>
            <GetStartedInputField placeholder="Type your website's domain..."/>
            <GetStartedButton type="submit" onClick={handleGetStarted}>Get Started &lt; &gt;</GetStartedButton>
        </GetStartedInputDiv>
    );
};

export default InputFieldGetStarted;