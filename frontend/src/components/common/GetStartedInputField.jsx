import React from 'react';
import { Link } from 'react-router-dom';
import '../../styles/components/GetStartedInputField.css'

function GetStartedInputField() {
    return (
        <div className="HomePage-Description-Input">
            <input type="text" className="Input-Field" placeholder="Type your website's domain..."/>
            <button className="GetStarted" type="submit">Get Started &lt; &gt;</button>
        </div>
    );
};

export default GetStartedInputField;
