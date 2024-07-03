import styled from "styled-components";

export const StaticMessageContainerDiv = styled.form`
    // width: 80%;
    display: flex;
    flex-direction:column;
    height : auto;
    padding: 1.5rem;              
    margin: 1rem;      
    background-color: white;    
    border:0px;
    border-radius: 0.5rem;     
    box-shadow: 0px 4px 4px 0px rgba(0, 0, 0, 0.25); 
`;

export const QuestionContainerDiv = styled.div`
    font-weight: 400;
    margin: 0.5rem;
`;

export const OptionContainerDiv = styled.div`
    width: 80%
    margin: 0.5rem;
    box-sizing: border-box;
`;

export const OptionDiv = styled.div`

`;

export const DescriptionTextArea = styled.textarea`
    width: 100%;
    height: 50px;
    margin: 0.25rem;
    padding: 0.5rem;
    box-sizing: border-box;
    border: 1px solid #000000;
    border-radius: 0.25rem;
    &::placeholder {
        color: #797e79;
        font-size: 14px;
        font-weight: 400;
    }
`;

export const SubmitButton = styled.button`
    flex-grow:1;
    width: 150px;
    height: 100%;
    padding: 0.25rem;
    margin: 0.5rem;
    border: 0;
    border-radius:2rem;
    box-sizing: border-box; 
    background-color:#07297A;
    color: #ffffff; 
    font-size: 14px;
    @media (max-width: 1100px) {
        &::placeholder{
            font-size: 12px;
        }
    }
`;