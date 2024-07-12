import React, { useState, useEffect } from "react";
import GrapesEditor from "../../src/components/pages/ShowOutput/GrapesEditor";
import BottomBar from "../../src/components/pages/ShowOutput/BottomBar";
import { ShowOutputContainer } from "../../src/styles/pages/ShowOutput";
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

  const createAndDownloadZip = async () => {
    try {
      // Create the zip file
      const createResponse = await fetch("http://localhost:8080/create-zip");
      if (!createResponse.ok) {
        throw new Error("Failed to create zip file");
      }

      // Download the zip file
      const downloadResponse = await fetch(
        "http://localhost:8080/download-zip"
      );
      if (!downloadResponse.ok) {
        throw new Error("Failed to download zip file");
      }
      const blob = await downloadResponse.blob();
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = url;
      a.download = "static.zip";
      document.body.appendChild(a);
      a.click();
      a.remove();
    } catch (error) {
      console.error("Error downloading zip file:", error);
    }
  };

  useEffect(() => {
    fetchHtmlFiles();
  }, []);

  return (
    <ShowOutputContainer>
      <GrapesEditor
        htmlContent={htmlContent}
        cssContent={cssContent}
        onSaveHtml={handleSaveHtml}
        onSaveCss={handleSaveCss}
        onLinkClick={fetchContent}
      />
      <BottomBar
        fetchPreviousFile={fetchPreviousFile}
        fetchNextFile={fetchNextFile}
        currentFile={currentFile}
        downloadZip={createAndDownloadZip}
      />
    </ShowOutputContainer>
  );
};

export default ShowOutput;
