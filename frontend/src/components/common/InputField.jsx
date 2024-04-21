import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import SendIcon from '@mui/icons-material/Send';

function InputField(onChange, onClick) {
    return (
        <div className="SendMessage">
            <input
                type={'text'}
                id='message'
                onChange={onChange}
                placeholder="Type your message..."
            />
            <button type="submit" className="" onClick={onClick}>
                <SendIcon className="Send-Icon" />
            </button>
        </div>
    );
}

export default InputField;