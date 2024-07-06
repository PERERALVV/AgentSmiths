import {
  LeftHolderDiv,
  LeftHolderImage,
} from "../../../styles/pages/ChatInterface";
import BrandName from "../../common/BrandName";

function ChatLeftHolder() {
  return (
    <LeftHolderDiv>
      <BrandName />
      <LeftHolderImage src="ReqChat2.gif" alt="Unprocessed Image" />
    </LeftHolderDiv>
  );
}

export default ChatLeftHolder;
