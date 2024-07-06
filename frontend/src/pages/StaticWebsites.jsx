import ChatLeftHolder from "../components/pages/Chat Interface/ChatLeftHolder";
import StaticChatMiddleHolder from "../components/pages/Chat Interface/StaticChatMiddleHolder";
import { ChatInterfaceDiv } from "../styles/pages/ChatInterface";

function StaticWebsites() {
  return (
    <ChatInterfaceDiv>
      <ChatLeftHolder />
      <StaticChatMiddleHolder />
    </ChatInterfaceDiv>
  );
}

export default StaticWebsites;
