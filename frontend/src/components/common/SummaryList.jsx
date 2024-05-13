import React, { useState, useEffect } from 'react';
import { SummaryListDiv } from '../../styles/components/SummaryList';

const name = "Gayuni's Boutique";
const type = "Gayuni's Boutique";
const functionalities = "Gayuni's Boutique";
const sellingPoints = "Gayuni's Boutique";

function SummaryList() {
  return (
    <SummaryListDiv>
      {name && <p>Name: <br/>{name}</p>}  {/* Display name only if it exists in data */}
      {type && <p>Type: <br/>{type}</p>}  
      {functionalities && <p>Functionalities: <br/>{functionalities}</p>}  
      {sellingPoints && <p>Type: <br/>{sellingPoints}</p>}  
    </SummaryListDiv>
  );
};

export default SummaryList;
