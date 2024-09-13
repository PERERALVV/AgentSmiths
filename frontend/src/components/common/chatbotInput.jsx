import { MessageInput } from "@chatscope/chat-ui-kit-react";
import {
  StyledMessageInput,
  StyledInputContainer,
} from "../../styles/components/chatBotInput";

const ChatbotInput = ({ handleSend }) => {
  return (
    <StyledInputContainer>
      <StyledMessageInput>
        <MessageInput
          style={{
            display: "flex",
            padding: "9.611px 8.543px 9.611px 17.085px",
            alignItems: "center",
            gap: "12.814px",
            flex: "1 0 0",
            alignSelf: "stretch",
          }}
          placeholder="Type message here"
          sendButton={true}
          attachButton={false}
          autoFocus={true}
          fancyScroll={true}
          activateAfterChange={true}
          onSend={handleSend}
        />
      </StyledMessageInput>
    </StyledInputContainer>
  );
};
export default ChatbotInput;

// import {MessageInput} from '@chatscope/chat-ui-kit-react';
// import {StyledMessageInput,StyledInputContainer} from "../../styles/components/chatBotInput"

// const ChatbotInput = ({ handleSend }) => {
//     return (
//         <StyledInputContainer>
//             <StyledMessageInput>
//                 <MessageInput
//                     style={{
//                         display: 'flex',
//                         padding: '9.611px 8.543px 9.611px 17.085px',
//                         alignItems: 'center',
//                         gap: '12.814px',
//                         flex: '1 0 0',
//                         alignSelf: 'stretch'
//                     }}
//                     placeholder="Type message here"
//                     sendButton={true}
//                     attachButton={false}
//                     autoFocus={true}
//                     fancyScroll={true}
//                     activateAfterChange={true}
//                     onSend={handleSend}
//                 />
//             </StyledMessageInput>
//         </StyledInputContainer>
//     )
// }
// export default ChatbotInput;
