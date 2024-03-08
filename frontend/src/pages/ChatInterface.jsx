import '../styles/pages/ChatInterface.css';
import ChatInterfaceConnection from '../components/common/ChatInterfaceConnection';

function ChatInterface() {
  return (
    <div className="chatInterface">
        <div className="chatInterface-holder">
            <div className="leftHolder">
                Agent Smiths
            </div>
            <div className="middleHolder">
                <ChatInterfaceConnection/>
            </div>
            <div className="rightHolder">
                
            </div>
        </div>
    </div>
  );
}

export default ChatInterface;
