import FaqItem from "../components/pages/Support/FaqItem";
import Support_Menu from "../components/pages/Support/support_menu";
import ChatBot from "../components/pages/Support/Chatbot";

import React, { useState } from "react";
import {
  SupportRoot,
  HomeNavbar,
  Navbar,
  NavbarChild,
  Agentsmith,
  HomeWrapper,
  Home,
  AgentSmithLabel,
  Support1,
  LogInButton,
  Service,
  ContactUsWrapper,
  ContactUs,
  LoginWrapper,
  Login,
  FaqMenuContainerParent,
  FaqMenuContainer,
} from "../styles/pages/Support";
const Support = () => {
  const [active, setActive] = useState(0);
  return (
    <SupportRoot>
      <HomeNavbar>
        <Navbar>
          <NavbarChild />
          <Agentsmith>Agentsmith</Agentsmith>
          <HomeWrapper>
            <Home>Home</Home>
          </HomeWrapper>
          <AgentSmithLabel>
            <Support1>Support</Support1>
          </AgentSmithLabel>
          <LogInButton>
            <Service>Service</Service>
          </LogInButton>
          <ContactUsWrapper>
            <ContactUs>Contact us</ContactUs>
          </ContactUsWrapper>
        </Navbar>
        <LoginWrapper>
          <Login
            disableElevation={true}
            variant="contained"
            sx={{
              textTransform: "none",
              color: "#fff",
              fontSize: "28",
              background: "#0d1b2a",
              borderRadius: "0px 25px 25px 0px",
              "&:hover": { background: "#0d1b2a" },
              height: 66,
            }}
          >
            LogIn
          </Login>
        </LoginWrapper>
      </HomeNavbar>
      <FaqMenuContainerParent>
        <FaqMenuContainer>
          <FaqItem />
          <FaqItem />
          <FaqItem />
        </FaqMenuContainer>
        {active === 0 && <Support_Menu setActive={setActive} />}
        {active === 1 && <ChatBot setActive={setActive} />}
      </FaqMenuContainerParent>
    </SupportRoot>
  );
};

export default Support;
