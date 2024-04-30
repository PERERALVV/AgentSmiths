import '../styles/pages/ChatInterface.css';
import ChatLeftHolder from '../components/pages/ChatLeftHolder';
import ChatMiddleHolder from '../components/pages/ChatMiddleHolder';
import ChatRightHolder from '../components/pages/ChatRightHolder';

function ChatInterface() {
  return (
    <div className="chatInterface">
        <div className="chatInterface-holder">
            <ChatLeftHolder/>
            <ChatMiddleHolder/>
            <ChatRightHolder/>
        </div>
    </div>
  );
}

export default ChatInterface;
