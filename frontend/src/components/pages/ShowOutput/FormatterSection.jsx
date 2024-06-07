import React, { useState, useEffect } from "react";
import GrapesEditor from "./GrapesEditor";
import { GrapesEditorCon } from "../../../styles/pages/ShowOutput";

const FormatterSection = () => {
  const [htmlContent, setHtmlContent] = useState("<p>hello</p>");

  useEffect(() => {
    const fetchHtmlContent = async () => {
      try {
        const response = await fetch("../../../../public/index.html");
        const text = await response.text();
        setHtmlContent(text);
      } catch (error) {
        console.error("Failed to load HTML content:", error);
      }
    };

    fetchHtmlContent();
  }, []);

  const handleSave = async (newHtml) => {
    try {
      const response = await fetch("/api/save-html", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ html: newHtml }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log("HTML saved successfully:", data);
      } else {
        console.error("Failed to save HTML");
      }
    } catch (error) {
      console.error("Error saving HTML:", error);
    }
  };

  return (
    <GrapesEditorCon>
      {htmlContent ? (
        <GrapesEditor initialHtml={htmlContent} onSave={handleSave} />
      ) : (
        <p>Loading HTML content...</p>
      )}
    </GrapesEditorCon>
  );
};

export default FormatterSection;
