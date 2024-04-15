import Chat from '../components/common/Chat';
import '../styles/pages/ChatInterface.css';
// import Chat from '../components/common/Chat';

function ChatInterface() {
  return (
    <div className="chatInterface">
        <div className="chatInterface-holder">
            <div className="leftHolder">
                Agent Smiths
            </div>
            <div className="middleHolder">
                <Chat/>
            </div>
            <div className="rightHolder">
                
            </div>
        </div>
    </div>
  );
}

export default ChatInterface;
