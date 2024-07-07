// src/components/Card.jsx
import React from "react";
import { StyledCard } from "../../../styles/pages/ContactUsStyle";

const Card = ({ children, selected, onClick }) => {
  return (
    <StyledCard selected={selected} onClick={onClick}>
      {children}
    </StyledCard>
  );
};

export default Card;
