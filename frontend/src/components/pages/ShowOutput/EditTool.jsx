import React from "react";
import ColorEditor from "./ColorEditor";
import FontEditor from "./FontEditor";
import TextEditor from "./TextEditor";
import { EditToolCon } from "../../../styles/pages/ShowOutput";

const EditTool = ({ activeComponent }) => {
  return (
    <EditToolCon>
      {activeComponent === "1" ? (
        <ColorEditor />
      ) : activeComponent === "2" ? (
        <FontEditor />
      ) : (
        <TextEditor />
      )}
    </EditToolCon>
  );
};

export default EditTool;
