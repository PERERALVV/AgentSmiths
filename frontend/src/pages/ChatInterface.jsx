import ChatLeftHolder from "../components/pages/Chat Interface/ChatLeftHolder";
import ChatMiddleHolder from "../components/pages/Chat Interface/ChatMiddleHolder";
import ChatRightHolder from "../components/pages/Chat Interface/ChatRightHolder";
import ChatOverlay from "../layouts/ChatOverlay";
import { ChatInterfaceDiv } from "../styles/pages/ChatInterface";

function ChatInterface() {
  return (
    <ChatInterfaceDiv>
      <ChatOverlay />
      <ChatLeftHolder />
      <ChatMiddleHolder />
      <ChatRightHolder />
    </ChatInterfaceDiv>
  );
}

export default ChatInterface;
