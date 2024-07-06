import React from 'react';
import { Link } from 'react-router-dom';
// import '../../styles/components/BrandName.css'; 
import { BrandNameDiv } from '../../styles/components/BrandName';

function BrandName({ color }) {
    return (
            <BrandNameDiv color={color}>
                AgentSmiths
            </BrandNameDiv>
    );
};

export default BrandName;
