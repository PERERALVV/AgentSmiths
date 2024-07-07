// FormatterSection.jsx

import React from "react";

const FormatterSection = ({ onFormat }) => {
  return (
    <div style={{ padding: "10px", backgroundColor: "#f0f0f0" }}>
      <button
        onClick={onFormat}
        style={{
          padding: "10px",
          fontSize: "16px",
          cursor: "pointer",
          backgroundColor: "#4CAF50",
        }}
      >
        Format HTML
      </button>
    </div>
  );
};

export default FormatterSection;
