import React, { useEffect, useRef } from "react";
import grapesjs from "grapesjs";
import "grapesjs/dist/css/grapes.min.css";

const GrapesEditor = ({ initialHtml, onSave }) => {
  const editorRef = useRef(null);
  const editorInstance = useRef(null);

  useEffect(() => {
    if (editorRef.current && !editorInstance.current) {
      editorInstance.current = grapesjs.init({
        container: editorRef.current,
        fromElement: true,
        storageManager: false, // We will handle saving manually
      });

      editorInstance.current.on("update", () => {
        const html = editorInstance.current.getHtml();
        onSave(html);
      });

      // Set the initial HTML after the editor is initialized
      editorInstance.current.setComponents(initialHtml);
    }

    return () => {
      if (editorInstance.current) {
        editorInstance.current.destroy();
        editorInstance.current = null;
      }
    };
  }, [initialHtml, onSave]);

  useEffect(() => {
    if (editorInstance.current) {
      editorInstance.current.setComponents(initialHtml);
    }
  }, [initialHtml]);

  return <div ref={editorRef}></div>;
};

export default GrapesEditor;
