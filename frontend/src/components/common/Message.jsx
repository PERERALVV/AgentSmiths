import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';

function Message({ content }) {
  if (content.type === 'join')
    return (
      <div className="card p-3 mb-2 bg-white rounded shadow-sm">
        <p>{`${content.sid} just joined`}</p>
      </div>
    );

  if (content.type === 'chat')
    return (
      <div className="">
        <div className="row justify-content-end"> {/* Align items to the right */}
          <div className="col-sm-8"> {/* Limit width to 80% of maximum width */}
            <div className="card p-3 mb-2 bg-white rounded shadow-sm">
              <p>{`${content.sid}:${content.message}`}</p>
            </div>
          </div>
          <div className="col-auto">
            <img src="ServerBotIcon.png" alt="Profile" className="rounded-circle mr-3" style={{ width: '40px', height: '40px' }} />
          </div>
        </div>
      </div>
    );

  if (content.type === 'chat_response')
    return (
      <div className="">
        <div className="row justify-content-start"> {/* Align items to the left */}
          <div className="col-auto">
            <img src="ServerBotIcon.png" alt="Profile" className="rounded-circle mr-3" style={{ width: '40px', height: '40px' }} />
          </div>
          <div className="col-sm-8"> {/* Limit width to 80% of maximum width */}
            <div className="card p-3 mb-2 bg-white rounded shadow-sm">
              <p>
                <strong>Response:</strong> {`${content.sid}:${content.message}`}
              </p>
            </div>
          </div>
        </div>
      </div>
    );
}

export default Message;
