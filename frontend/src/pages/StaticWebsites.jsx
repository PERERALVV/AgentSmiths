import ChatLeftHolder from '../components/pages/ChatLeftHolder';
import StaticChatMiddleHolder from '../components/pages/StaticChatMiddleHolder';
import { ChatInterfaceDiv } from '../styles/pages/ChatInterface';

function StaticWebsites() {
  return (
    <ChatInterfaceDiv>
            <ChatLeftHolder/>
            <StaticChatMiddleHolder/>
    </ChatInterfaceDiv>
  );
}

export default StaticWebsites;
