function Message({content}) {
    if(content.type==='join')
      return(
        <p>
          {`${content.sid} just joined`}
        </p>
      );
  
    if(content.type==='chat')
      return(
        <p>
          {`${content.sid}:${content.message}`}
        </p>
      );

    if(content.type==='chat_response')
      return(
        <p>
          <strong>Response:</strong>
          {`${content.sid}:${content.message}`}
        </p>
      );
  }
  
  export default Message;