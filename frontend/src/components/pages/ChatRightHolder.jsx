import { RightHolderDiv } from '../../styles/components/ChatHolders';
import { GradientTextDiv } from '../../styles/components/GradientText';
import SummaryList from '../common/SummaryList';

function ChatRightHolder() {
  // Hardcoded sample data
  const webName = "Gayuni's Boutique";

  return (
    <RightHolderDiv>
      <GradientTextDiv>
        {webName}
      </GradientTextDiv>
      <SummaryList/>
    </RightHolderDiv>
  );
}

export default ChatRightHolder;