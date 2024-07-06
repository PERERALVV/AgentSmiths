import styled from "styled-components";

export const Title = styled.div`
    font-weight:800;
    line-height: 0;
    color: ${(props) => props.color || '#0D1B2A'};
    font-size: ${(props) => props.fontSize|| '50px'};
    // @media (max-width: 1100px) {
    //         font-size: calc(28px + (35 - 28) * ((100vw - 800px) / (1100 - 800)));
    // }
`;

