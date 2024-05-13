import { LeftHolderDiv, LeftHolderImage } from '../../styles/components/ChatHolders';
import BrandName from '../common/BrandName';

function ChatLeftHolder() {
  return (
    <LeftHolderDiv>
        <BrandName/>
        <LeftHolderImage src="ChatLeftHolderImage.png" alt="Unprocessed Image"/>
    </LeftHolderDiv>
  );
}

export default ChatLeftHolder;
