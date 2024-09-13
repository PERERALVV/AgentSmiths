import { Button } from "@mui/material";
import styled from "styled-components";

export const NavbarChild = styled.div`
  height: 66px;
  width: 1527px;
  position: relative;
  border-radius: var(--br-6xl) 0px 0px var(--br-6xl);
  background-color: var(--color-gray-200);
  display: none;
  max-width: 100%;
`;
export const Agentsmith = styled.b`
  position: relative;
  z-index: 1;
`;
export const Home = styled.b`
  position: relative;
  display: inline-block;
  min-width: 95px;
  z-index: 1;
`;
export const HomeWrapper = styled.div`
  width: 157px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-12xs) 0px 0px;
  box-sizing: border-box;
`;
export const Support1 = styled.b`
  position: relative;
  display: inline-block;
  min-width: 128px;
  z-index: 1;
`;
export const AgentSmithLabel = styled.div`
  width: 174px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
`;
export const Service = styled.b`
  position: relative;
  display: inline-block;
  min-width: 101px;
  z-index: 1;
`;
export const LogInButton = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-9xs) var(--padding-15xl) 0px 0px;
  font-size: var(--font-size-9xl);
`;
export const ContactUs = styled.b`
  position: relative;
  white-space: nowrap;
  z-index: 1;
`;
export const ContactUsWrapper = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-12xs) 0px 0px;
`;
export const Navbar = styled.div`
  flex: 1;
  border-radius: var(--br-6xl) 0px 0px var(--br-6xl);
  background-color: var(--color-gray-200);
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: space-between;
  padding: var(--padding-2xs) var(--padding-60xl) var(--padding-3xs)
    var(--padding-33xl);
  box-sizing: border-box;
  max-width: 100%;
  gap: var(--gap-xl);
  @media screen and (max-width: 1425px) {
    padding-left: var(--padding-7xl);
    padding-right: var(--padding-20xl);
    box-sizing: border-box;
  }
`;
export const Login = styled(Button)`
  align-self: stretch;
  height: 66px;
`;
export const LoginWrapper = styled.div`
  width: 197px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-12xs) 0px 0px;
  box-sizing: border-box;
`;
export const HomeNavbar = styled.header`
  width: 1745px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: var(--gap-2xl);
  max-width: 100%;
  text-align: left;
  font-size: var(--font-size-13xl);
  color: var(--color-white);
  font-family: var(--font-open-sans);
`;
export const FaqMenuContainer = styled.section`
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  gap: var(--gap-55xl);
  max-width: 100%;
  @media screen and (max-width: 1200px) {
    gap: 37px 74px;
    min-width: 100%;
  }
  @media screen and (max-width: 825px) {
    gap: 18px 74px;
  }
`;
export const FaqMenuChild = styled.div`
  height: 524px;
  width: 476px;
  position: relative;
  border-radius: var(--br-6xl);
  background-color: var(--color-gainsboro);
  display: none;
  max-width: 100%;
`;
export const FrameChild = styled.img`
  width: 34px;
  height: 30.9px;
  position: relative;
  object-fit: contain;
  mix-blend-mode: normal;
`;
export const MenuItemInner = styled.div`
  height: 33.9px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-10xs) 0px 0px;
  box-sizing: border-box;
`;
export const CategoryType = styled.b`
  position: relative;
  @media screen and (max-width: 450px) {
    font-size: var(--font-size-xl);
  }
`;
export const MenuItem1 = styled.div`
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: var(--gap-xs);
`;
export const GreetingMessageIcon = styled.img`
  width: 30.9px;
  height: 34px;
  position: relative;
  object-fit: contain;
  mix-blend-mode: normal;
  flex-shrink: 0;
  debug_commit: f6aba90;
`;
export const SupportBotContainer = styled.div`
  height: 35.5px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 1.5px 0px 0px;
  box-sizing: border-box;
`;
export const CategoryType1 = styled.b`
  position: relative;
  flex-shrink: 0;
  debug_commit: f6aba90;
  @media screen and (max-width: 450px) {
    font-size: var(--font-size-xl);
  }
`;
export const MenuItem2 = styled.div`
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 13.600000000000364px;
`;
export const MenuItems = styled.div`
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-start;
  gap: 42px;
  z-index: 1;
`;
export const FaqMenu = styled.div`
  align-self: stretch;
  height: 524px;
  border-radius: var(--br-6xl);
  background-color: var(--color-gainsboro);
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-7xl) 49px;
  box-sizing: border-box;
  max-width: 100%;
  @media screen and (max-width: 450px) {
    padding-left: var(--padding-xl);
    padding-right: var(--padding-xl);
    box-sizing: border-box;
  }
`;
export const SupportBotChild = styled.div`
  height: 136px;
  width: 472px;
  position: relative;
  border-radius: var(--br-31xl) var(--br-31xl) 0px var(--br-31xl);
  background-color: var(--color-gainsboro-100);
  display: none;
  max-width: 100%;
`;
export const Hey = styled.p`
  margin: 0;
`;
export const HeyImHereToContainer = styled.h3`
  margin: 0;
  position: relative;
  font-size: inherit;
  font-weight: 700;
  font-family: inherit;
  z-index: 1;
  @media screen and (max-width: 825px) {
    font-size: var(--font-size-10xl);
  }
  @media screen and (max-width: 450px) {
    font-size: var(--font-size-3xl);
  }
`;
export const Download1Icon = styled.img`
  width: 85px;
  height: 85px;
  position: relative;
  border-radius: var(--br-81xl);
  object-fit: cover;
  z-index: 1;
`;
export const Download1Wrapper = styled.div`
  height: 89px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-start;
  padding: var(--padding-9xs) 0px 0px;
  box-sizing: border-box;
`;
export const SupportBot = styled.div`
  align-self: stretch;
  border-radius: var(--br-31xl) var(--br-31xl) 0px var(--br-31xl);
  background-color: var(--color-gainsboro-100);
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  padding: 15px 38px 23px;
  box-sizing: border-box;
  gap: 11px;
  max-width: 100%;
  font-size: var(--font-size-17xl);
  color: var(--color-gray-200);
  @media screen and (max-width: 825px) {
    flex-wrap: wrap;
  }
`;
export const FaqMenuParent = styled.div`
  width: 476px;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: flex-start;
  gap: var(--gap-55xl);
  min-width: 476px;
  max-width: 100%;
  @media screen and (max-width: 1425px) {
    flex: 1;
  }
  @media screen and (max-width: 825px) {
    gap: 37px 74px;
    min-width: 100%;
  }
`;
export const FaqMenuContainerParent = styled.main`
  width: 1740px;
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  justify-content: flex-start;
  gap: 101px;
  max-width: 100%;
  text-align: left;
  font-size: var(--font-size-6xl);
  color: var(--color-black);
  font-family: var(--font-open-sans);
  @media screen and (max-width: 1425px) {
    flex-wrap: wrap;
  }
  @media screen and (max-width: 825px) {
    gap: 101px 50px;
  }
  @media screen and (max-width: 450px) {
    gap: 101px 25px;
  }
`;
export const SupportRoot = styled.div`
  width: 100%;
  position: relative;
  background-color: var(--color-white);
  overflow: hidden;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  padding: var(--padding-24xl) var(--padding-xl) 80px;
  box-sizing: border-box;
  gap: var(--gap-55xl);
  letter-spacing: normal;
  @media screen and (max-width: 825px) {
    gap: 37px 74px;
  }
  @media screen and (max-width: 450px) {
    gap: 18px 74px;
  }
`;
