import ChatLeftHolder from '../components/pages/ChatLeftHolder';
import ChatMiddleHolder from '../components/pages/ChatMiddleHolder';
import ChatRightHolder from '../components/pages/ChatRightHolder';
import ChatOverlay from '../layouts/ChatOverlay';
import { ChatInterfaceDiv } from '../styles/pages/ChatInterface';

function ChatInterface() {
  return (
    <ChatInterfaceDiv>
      <ChatOverlay/>
            <ChatLeftHolder/>
            <ChatMiddleHolder/>
            <ChatRightHolder/>
    </ChatInterfaceDiv>
  );
}

export default ChatInterface;
