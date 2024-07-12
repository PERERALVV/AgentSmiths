import React from "react";
import {
  BottomBarContainer,
  NavigationButton,
  ButtonImage,
  CurrentFile,
  RightDiv,
  DownloadDiv,
} from "../../../styles/pages/ShowOutput";

const BottomBar = ({
  fetchPreviousFile,
  fetchNextFile,
  currentFile,
  downloadZip,
}) => {
  return (
    <BottomBarContainer>
      <NavigationButton onClick={fetchPreviousFile}>
        <ButtonImage
          src={"./images/previous.png"}
          alt="Previous"
          style={{ marginRight: "5px" }}
        />
        Previous&nbsp;&nbsp;
      </NavigationButton>
      <CurrentFile>{currentFile}</CurrentFile>
      <RightDiv>
        <DownloadDiv onClick={downloadZip}>
          <ButtonImage
            src={"./images/download.png"}
            alt="Download"
            style={{ margin: "0px" }}
          />
        </DownloadDiv>

        <NavigationButton onClick={fetchNextFile}>
          &nbsp;&nbsp;Next
          <ButtonImage
            src={"./images/next.png"}
            alt="Next"
            style={{ marginLeft: "5px" }}
          />
        </NavigationButton>
      </RightDiv>
    </BottomBarContainer>
  );
};

export default BottomBar;
