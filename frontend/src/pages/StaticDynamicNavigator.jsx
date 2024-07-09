import React from "react";
import { useNavigate } from "react-router-dom";
import {
  MainContainer,
  Card,
  CardTitle,
  CardDetails,
  Button,
  CardDetailsContainer,
} from "../styles/pages/StaticDynamicNavigator";

const StaticDynamicNavigator = () => {
  const navigate = useNavigate();

  const navigateToStaticWebsites = () => {
    navigate("/staticwebsites");
  };

  const navigateToDynamicWebsites = () => {
    navigate("/chat");
  };

  return (
    <MainContainer>
      <Card>
        <CardTitle>Static Websites</CardTitle>
        <hr />
        <CardDetailsContainer>
          <br />
          <CardDetails>• Generates only HTML and CSS files</CardDetails>
          <CardDetails>
            • UI customization with an easy editor interface
          </CardDetails>
          <CardDetails>• Preview the website before downloading</CardDetails>
          <CardDetails>• Easy to save and download</CardDetails>
        </CardDetailsContainer>
        <hr />
        <Button onClick={navigateToStaticWebsites}>Try static</Button>
      </Card>
      <Card>
        <CardTitle>Dynamic Websites</CardTitle>
        <hr />
        <CardDetailsContainer>
          <br />
          <CardDetails>• Generates a React project</CardDetails>
          <CardDetails>• No customization or preview available</CardDetails>
          <CardDetails>• Easy to download</CardDetails>
        </CardDetailsContainer>
        <hr />
        <Button onClick={navigateToDynamicWebsites}>Try dynamic</Button>
      </Card>
    </MainContainer>
  );
};

export default StaticDynamicNavigator;
