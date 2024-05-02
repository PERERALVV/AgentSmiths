import React from "react";
import { GoogleFontLoader } from "react-google-fonts";

const FontEditor = () => {
  return (
    <div style={{ backgroundColor: "blue" }}>
      font editor
      <GoogleFontLoader fonts={[{ font: "Roboto", weights: [400, 700] }]} />
    </div>
  );
};

export default FontEditor;
