import { GradientTextDiv } from '../../styles/components/GradientText';
import { RightHolderDiv, RightHolderImage } from '../../styles/pages/ChatInterface';

function ChatRightHolder() {

  return (
    <RightHolderDiv>
      <RightHolderImage src="RightHolder.gif" alt="Unprocessed Image"/>
      <GradientTextDiv>
        Building ...
      </GradientTextDiv>
    </RightHolderDiv>
  );
}

export default ChatRightHolder;