import ChatLeftHolder from '../components/pages/ChatLeftHolder';
import ChatMiddleHolder from '../components/pages/ChatMiddleHolder';
import ChatRightHolder from '../components/pages/ChatRightHolder';
import { ChatInterfaceDiv } from '../styles/pages/ChatInterface';

function ChatInterface() {
  return (
    <ChatInterfaceDiv>
            <ChatLeftHolder/>
            <ChatMiddleHolder/>
            <ChatRightHolder/>
    </ChatInterfaceDiv>
  );
}

export default ChatInterface;
