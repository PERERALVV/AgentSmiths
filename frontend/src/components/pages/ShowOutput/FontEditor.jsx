import React, { useState } from "react";
import FontEditorChild from "./FontEditorChild";

const FontEditor = () => {
  const [selectedFont, setSelectedFont] = useState("");

  const handleFontChange = (font) => {
    console.log("Selected font:", font);
    setSelectedFont(font);
  };

  return (
    <div>
      <h1 style={{ fontFamily: selectedFont }}>Font Preview</h1>
      <FontEditorChild onChange={handleFontChange} />
    </div>
  );
};

export default FontEditor;
