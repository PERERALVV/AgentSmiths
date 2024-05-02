import React, { useState } from "react";
import FormatterSection from "../components/pages/ShowOutput/FormatterSection";
import BottomBar from "../components/pages/ShowOutput/BottomBar";
import EditTool from "../components/pages/ShowOutput/EditTool";
import {
  ShowOutputCon,
  ShowOutputMiddle,
  NavCon,
  Button,
  ButtonCon,
  EditToolContainer,
  FormatterSectionCon,
} from "../styles/pages/ShowOutput";

const ShowOutput = () => {
  const [activeButton, setActiveButton] = useState(null);
  const [activeComponent, setActiveComponent] = useState(null);

  const handleClick = (index) => {
    setActiveButton(index);
    setActiveComponent(index);
  };

  return (
    <ShowOutputCon>
      <NavCon>
        <ButtonCon>
          <Button
            style={{ borderRadius: "25px 0px 0px 25px" }}
            onClick={() => {
              handleClick("1");
            }}
            active={activeButton === "1"}
          >
            Color Editor
          </Button>
          <Button
            style={{ borderRadius: "0px" }}
            onClick={() => {
              handleClick("2");
            }}
            active={activeButton === "2"}
          >
            Font Editor
          </Button>
          <Button
            style={{ borderRadius: "0px" }}
            onClick={() => {
              handleClick("3");
            }}
            active={activeButton === "3"}
          >
            Text Editor
          </Button>
          <Button style={{ borderRadius: "0px 25px 25px 0px" }}>
            Speak with an Agent
          </Button>
        </ButtonCon>
      </NavCon>
      <ShowOutputMiddle>
        <FormatterSectionCon>
          <FormatterSection />
        </FormatterSectionCon>
        <EditToolContainer>
          {activeComponent && <EditTool activeComponent={activeComponent} />}
        </EditToolContainer>
      </ShowOutputMiddle>
      <BottomBar />
    </ShowOutputCon>
  );
};

export default ShowOutput;
