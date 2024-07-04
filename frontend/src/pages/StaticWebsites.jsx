import ChatLeftHolder from '../components/pages/ChatLeftHolder';
import ChatRightHolder from '../components/pages/ChatRightHolder';
import StaticChatMiddleHolder from '../components/pages/StaticChatMiddleHolder';
import { ChatInterfaceDiv } from '../styles/pages/ChatInterface';

function StaticWebsites() {
  return (
    <ChatInterfaceDiv>
            <ChatLeftHolder/>
            <StaticChatMiddleHolder/>
            <ChatRightHolder/>
    </ChatInterfaceDiv>
  );
}

export default StaticWebsites;
