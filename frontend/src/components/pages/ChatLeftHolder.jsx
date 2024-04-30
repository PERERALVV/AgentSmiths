import { LeftHolderDiv, LeftHolderImage } from '../../styles/components/ChatHolders';
import BrandName from '../common/BrandName';

function ChatLeftHolder() {
  return (
    <LeftHolderDiv>
    {/* <div className="leftHolder"> */}
        <BrandName/>
        <LeftHolderImage src="ChatLeftHolderImage.png" alt="Unprocessed Image"/>
    {/* </div> */}
    </LeftHolderDiv>
  );
}

export default ChatLeftHolder;
