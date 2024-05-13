import styled from "styled-components";

export const ConnectedBarDiv = styled.div`
    height: 40px;
    background-color: bisque;
    display: flex; /* Make it flex so it fills the width of the grey div */
    align-items: center; /* Center the content vertically */
    justify-content: flex-start; /* Align the content horizontally to the left */
    border-top-left-radius: 8px; /* Add rounded corners if the grey div has them */
    border-top-right-radius: 8px; /* Add rounded corners if the grey div has them */
    // justify-content: spece-between;
    // @media (max-width: 700px) {
    //     display: none;
    // }
`;
