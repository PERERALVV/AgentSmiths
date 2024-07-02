import styled from "styled-components";

export const BrandNameDiv = styled.div`
    color:#0D1B2A;
    font-size: 35px;
    font-weight: 700;
    line-height: normal;
    text-decoration: none;
    display: flex;
    justify-content: center;
    color: ${(props) => props.color || '#0D1B2A'};
    @media (max-width: 1100px) {
            font-size: calc(28px + (35 - 28) * ((100vw - 800px) / (1100 - 800)));
    }
    // @media (max-width: 800px) {
    //         font-size: 22px;
    // }
`;

