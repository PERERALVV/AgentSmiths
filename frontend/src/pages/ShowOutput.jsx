import React, { useState, useEffect } from "react";
import GrapesEditor from "../../src/components/pages/ShowOutput/GrapesEditor";
import prevIcon from "../images/previous.png";
import nextIcon from "../images/next.png";

const ShowOutput = () => {
  const [htmlContent, setHtmlContent] = useState("");
  const [cssContent, setCssContent] = useState("");
  const [currentFile, setCurrentFile] = useState("");
  const [htmlFiles, setHtmlFiles] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);

  const fetchContent = async (filename) => {
    try {
      console.log(`Fetching HTML and CSS content from backend for ${filename}`);
      const response = await fetch(
        `http://localhost:8080/get-html-css/${filename}`
      );
      if (!response.ok) {
        throw new Error("Failed to fetch content");
      }
      const data = await response.json();
      setHtmlContent(data.html);
      setCssContent(data.css || "");
      setCurrentFile(filename);
    } catch (error) {
      console.error("Error fetching content:", error);
    }
  };

  const fetchHtmlFiles = async () => {
    try {
      const response = await fetch("http://localhost:8080/get-html-files");
      if (!response.ok) {
        throw new Error("Failed to fetch HTML files list");
      }
      const data = await response.json();
      setHtmlFiles(data.files);
      if (data.files.length > 0) {
        fetchContent(data.files[0]);
        setCurrentIndex(0);
      }
    } catch (error) {
      console.error("Error fetching HTML files list:", error);
    }
  };

  const handleSaveHtml = async (html) => {
    try {
      console.log(`Saving HTML content to backend for ${currentFile}`);
      const response = await fetch("http://localhost:8080/save-html", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ filename: currentFile, html }),
      });
      if (!response.ok) {
        throw new Error("Failed to save HTML content");
      }
      alert("HTML content saved successfully");
    } catch (error) {
      console.error("Error saving content:", error);
      alert("Error saving HTML content");
    }
  };

  const handleSaveCss = async (css) => {
    try {
      const cssFilename = currentFile.replace(".html", ".css");
      console.log(`Saving CSS content to backend for ${cssFilename}`);
      const response = await fetch("http://localhost:8080/save-css", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ filename: cssFilename, css }),
      });
      if (!response.ok) {
        throw new Error("Failed to save CSS content");
      }
      alert("CSS content saved successfully");
    } catch (error) {
      console.error("Error saving content:", error);
      alert("Error saving CSS content");
    }
  };

  const fetchNextFile = () => {
    if (htmlFiles.length === 0) return;
    const nextIndex = (currentIndex + 1) % htmlFiles.length;
    fetchContent(htmlFiles[nextIndex]);
    setCurrentIndex(nextIndex);
  };

  const fetchPreviousFile = () => {
    if (htmlFiles.length === 0) return;
    const prevIndex = (currentIndex - 1 + htmlFiles.length) % htmlFiles.length;
    fetchContent(htmlFiles[prevIndex]);
    setCurrentIndex(prevIndex);
  };

  useEffect(() => {
    fetchHtmlFiles();
  }, []);

  return (
    <div style={{ display: "flex", flexDirection: "column", height: "100vh" }}>
      <GrapesEditor
        htmlContent={htmlContent}
        cssContent={cssContent}
        onSaveHtml={handleSaveHtml}
        onSaveCss={handleSaveCss}
        onLinkClick={fetchContent}
      />
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
          padding: "10px",
          backgroundColor: "#f0f0f0",
        }}
      >
        <button
          onClick={fetchPreviousFile}
          style={{
            padding: "10px",
            fontSize: "16px",
            cursor: "pointer",
            backgroundColor: "#4CAF50",
            borderRadius: "50px",
            border: "none",
            display: "flex",
            alignItems: "center",
          }}
        >
          <img
            src={prevIcon}
            alt="Previous"
            style={{ width: "30px", height: "30px", marginRight: "5px" }}
          />
          Previous
        </button>
        <span
          style={{ fontSize: "16px", margin: "0 20px", backgroundColor: "red" }}
        >
          {currentFile}
        </span>
        <button
          onClick={fetchNextFile}
          style={{
            padding: "10px",
            fontSize: "16px",
            cursor: "pointer",
            backgroundColor: "#4CAF50",
            borderRadius: "50px",
            border: "none",
            display: "flex",
            alignItems: "center",
          }}
        >
          Next
          <img
            src={nextIcon}
            alt="Next"
            style={{ width: "30px", height: "30px", marginLeft: "5px" }}
          />
        </button>
      </div>
    </div>
  );
};

export default ShowOutput;
