import React, { useState, useEffect } from "react";

const FontEditorChild = ({ onChange }) => {
  const [fonts, setFonts] = useState([]);
  const [selectedFont, setSelectedFont] = useState("");

  useEffect(() => {
    fetch(
      "https://www.googleapis.com/webfonts/v1/webfonts?key=AIzaSyB0g8CpYltBybAu1agE685z5bnFSZbePas"
    )
      .then((response) => response.json())
      .then((data) => {
        setFonts(data.items.map((font) => font.family));
      })
      .catch((error) => console.error("Error fetching fonts:", error));
  }, []);

  const handleFontChange = (event) => {
    const font = event.target.value;
    setSelectedFont(font);
    if (onChange) {
      onChange(font);
    } else {
      console.error("onChange is not provided");
    }
    };
    
  return (
    <div>
      <select value={selectedFont} onChange={handleFontChange}>
        <option value="">Select a font</option>
        {fonts.map((font) => (
          <option key={font} value={font} style={{ fontFamily: font }}>
            {font}
          </option>
        ))}
      </select>
      <div style={{ fontFamily: selectedFont }}>{selectedFont}</div>
    </div>
  );
};

export default FontEditorChild;
