import { GradientTextDiv } from '../../styles/components/GradientText';
import { RightHolderDiv } from '../../styles/pages/ChatInterface';
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