import React, { useState } from 'react';
import styled from 'styled-components';

const OverlayContainer = styled.div`
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5); /* Semi-transparent background */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000; /* High z-index to ensure it overlays other content */
`;

const OverlayContent = styled.div`
    background-color: white;
    padding: 2rem;
    border-radius: 1rem;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    text-align: center;
`;

const InstructionsDiv = styled.div`
    // text-align: left;
`;

const CloseButton = styled.button`
    background-color: #07297A; /* Example button color */
    color: white;
    border: none;
    padding: 0.5rem 1rem;
    border-radius: 0.5rem;
    cursor: pointer;
    font-size: 1rem;
    margin-top: 1rem;

    &:hover {
        background-color: #05468A; /* Darken on hover */
    }
`;

const ChatOverlay = () => {
    const [isVisible, setIsVisible] = useState(true);

    const handleClose = () => {
        setIsVisible(false);
    };

    return isVisible ? (
        <OverlayContainer>
            <OverlayContent>
                <h2>Instructions</h2>
                <InstructionsDiv>
                <p>It's time to meet our AI business analyst, AgentBA.</p>
                <p>When answering, please provide complete answers.</p>
                <p>Use the 'Help me answer' button to request clarification for questions.</p>
                <p>Once you answer or request help, your inputs and help requests will be disabled until 
                    the next response from AgentBA.</p>
                <p>AgentBA is cautious about prompt injections. After 3 attempts your session will 
                    be terminated.</p>
                <p>Failing to respond within 4 minutes will terminate your session.</p>
                <p>AgentBA is still learning to be better. We expect you to help AgentBA perform well</p>
                </InstructionsDiv>
                <CloseButton onClick={handleClose}>Close and Proceed</CloseButton>
            </OverlayContent>
        </OverlayContainer>
    ) : null;
};

export default ChatOverlay;
