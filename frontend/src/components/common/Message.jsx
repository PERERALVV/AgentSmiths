import React from 'react';
// import 'bootstrap/dist/css/bootstrap.min.css';
import { BaMessageBoxDiv, BaMessageDiv, JoinDiv, UserIconDiv, UserIconImage, UserMessageBoxDiv, UserMessageDiv, WarningMessageBoxDiv } from '../../styles/components/Message';

function Message({ content }) {
  if (content.type === 'join')
    return (
      <JoinDiv>
        <p>{`${content.sid} just joined`}</p>
      </JoinDiv>
    );

  if (content.type === 'chat')
    return (
        <UserMessageDiv>
            <UserMessageBoxDiv style={{backgroundColor:'#07297A'}}>
              {/* <p>{`${content.sid}:${content.message}`}</p> */}
              <p>{`${content.message}`}</p>
            </UserMessageBoxDiv>
            <UserIconDiv> {/* Hide on screens smaller than sm (576px) */}
              <UserIconImage src="ServerBotIcon.png" alt="Profile"  style={{ width: '40px', height: '40px' }}/>
            </UserIconDiv>
        </UserMessageDiv>
    );

  if (content.type === 'chat_response')
    return (
        <BaMessageDiv>
          <UserIconDiv> {/* Hide on screens smaller than sm (576px) */}
            <UserIconImage src="ServerBotIcon.png" alt="Profile"  style={{ width: '40px', height: '40px' }} />
          </UserIconDiv>
          <BaMessageBoxDiv>
            {/* <p><strong>Response:</strong> {`${content.sid}:${content.message}`}</p> */}
            <p>{`${content.message}`}</p>
          </BaMessageBoxDiv>
        </BaMessageDiv>
    );

    if (content.type === 'warning')
      return (
          <BaMessageDiv>
            <UserIconDiv> {/* Hide on screens smaller than sm (576px) */}
              <UserIconImage src="ServerBotIcon.png" alt="Profile"  style={{ width: '40px', height: '40px' }} />
            </UserIconDiv>
            <WarningMessageBoxDiv>
              {/* <p><strong>Response:</strong> {`${content.sid}:${content.message}`}</p> */}
              <p>{`${content.message}`}</p>
            </WarningMessageBoxDiv>
          </BaMessageDiv>
      );
}

export default Message;
