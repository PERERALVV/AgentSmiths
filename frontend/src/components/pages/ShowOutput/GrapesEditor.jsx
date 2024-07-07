// GrapesEditor.jsx

import React, { useEffect, useRef } from "react";
import grapesjs from "grapesjs";
import "grapesjs/dist/css/grapes.min.css";

const GrapesEditor = ({
  htmlContent,
  cssContent,
  onSaveHtml,
  onSaveCss,
  onLinkClick,
}) => {
  const editorRef = useRef(null);

  useEffect(() => {
    console.log("Initializing GrapesJS editor");
    const editor = grapesjs.init({
      container: editorRef.current,
      height: "100vh",
      width: "auto",
      storageManager: { type: "none" },
    });

    if (htmlContent) {
      console.log("Setting HTML content:", htmlContent);
      editor.setComponents(htmlContent);
    }

    if (cssContent) {
      console.log("Setting CSS content:", cssContent);
      editor.setStyle(cssContent);
    }

    editor.on("run:open-assets", () => {
      const iframe = editor.Canvas.getFrameEl();
      const iframeDoc = iframe.contentDocument;
      iframeDoc.addEventListener("click", (e) => {
        const target = e.target.closest("a");
        if (target && target.getAttribute("href")) {
          e.preventDefault();
          const filename = target.getAttribute("href");
          onLinkClick(filename);
        }
      });
    });

    editor.Panels.addButton("options", {
      id: "save-html-button",
      className: "fa fa-save",
      command: "save-html",
      attributes: { title: "Save HTML" },
      label: " HTML",
    });

    editor.Panels.addButton("options", {
      id: "save-css-button",
      className: "fa fa-save",
      command: "save-css",
      attributes: { title: "Save CSS" },
      label: " CSS",
    });

    editor.Commands.add("save-html", {
      run: async (editor) => {
        const html = editor.getHtml();
        await onSaveHtml(html);
      },
    });

    editor.Commands.add("save-css", {
      run: async (editor) => {
        const css = editor.getCss();
        await onSaveCss(css);
      },
    });

    return () => editor.destroy();
  }, [htmlContent, cssContent, onSaveHtml, onSaveCss, onLinkClick]);

  return <div id="gjs" ref={editorRef} style={{ height: "100%" }}></div>;
};

export default GrapesEditor;
