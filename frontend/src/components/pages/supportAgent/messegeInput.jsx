import React from 'react';
import styled from 'styled-components';
import { MessageInput as OriginalMessageInput } from '@chatscope/chat-ui-kit-react';

const MessageInputWrapper = ({ className, ...props }) => (
  <div className={className}>
    <OriginalMessageInput {...props} />
  </div>
);

const StyledMessageInput = styled(MessageInputWrapper)`
display: flex;
padding: 9.611px 8.543px 9.611px 17.085px;
align-items: center;
gap: 12.814px;
flex: 1 0 0;
align-self: stretch;
`;

export default StyledMessageInput;