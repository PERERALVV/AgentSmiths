import { MiddleHolderDiv } from '../../styles/components/ChatHolders';
import '../../styles/components/ChatHolders.css';
import { ConnectedBarDiv } from '../../styles/components/ConnectedBar';
import Chat from '../common/Chat';

function ChatMiddleHolder() {
  return (
    <MiddleHolderDiv>
        <Chat/>
    </MiddleHolderDiv>
  );
}

export default ChatMiddleHolder;
