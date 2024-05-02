import React, { useState } from "react";
import { ChromePicker } from "react-color";

const ColorEditor = () => {
  const [color, setColor] = useState("#ffffff");

  const handleChange = (pickedColor) => {
    setColor(pickedColor.rgb);
  };
  console.log(color);
  return (
    <div>
      <ChromePicker
        color={color}
        onChange={handleChange}
        disableAlpha={false}
        width="380px"
      />
      <h1
        style={{
          backgroundColor: `rgba(${color.r}, ${color.g}, ${color.b}, ${color.a})`,
          fontFamily: "monospace",
          fontSize: "20px",
          padding: "10px",
          color: "Black",
          textAlign: "center",
          borderRadius: "5px",
        }}
      >
        rgba({color.r}, {color.g}, {color.b}, {color.a})
      </h1>
    </div>
  );
};

export default ColorEditor;
