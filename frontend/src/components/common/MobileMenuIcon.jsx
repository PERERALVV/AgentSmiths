import React from 'react';
import { MobileMenuDiv, MobileMenuSpan } from '../../styles/layouts/NavBar';


function MobileMenuIcon({ onClick }) {
    return (
        <MobileMenuDiv onClick={onClick}>
            <MobileMenuSpan></MobileMenuSpan>
            <MobileMenuSpan></MobileMenuSpan>
            <MobileMenuSpan></MobileMenuSpan>
        </MobileMenuDiv>
    );
}

export default MobileMenuIcon;