import styled from 'styled-components';
import Box from '@mui/material/Box';
import { RichTreeView } from '@mui/x-tree-view/RichTreeView';
import { TreeItem2 } from '@mui/x-tree-view/TreeItem2';

// we can use this to categorize the faqs we create; just apply ayeshas categorization function again to the generated faqs

// or for simplysity just use some buttons to choose faq category to display the faqs of that category
const FaqMenu= ()=> {
    const MUI_X_PRODUCTS = [
        {
          id: 'grid',
          label: 'using the chatbot',
          children: [
            { id: 'grid-community',
               label: 'data collection',
               children:[
                { id:'grid-community-1',label:'how to collect data'},
                {id:'grid-community-2',label:'how to store data'}
              ] 
            },
            { id: 'grid-pro', label: 'human availability' },
            { id: 'grid-premium', label: 'got stuck??' },
          ],
        },
        {
          id: 'pickers',
          label: 'using the main chat',
          children: [
            { id: 'pickers-community', label: 'how to talk' },
            { id: 'pickers-pro', label: 'got stuck??' },
          ],
        },
      ];
    return (
        <FaqMenuContainer>
            <RichTreeView 
                items={MUI_X_PRODUCTS} 
                slots={{ 
                    item: StyledTreeItem
                }}
                sx={{StyledTreeView}}
            />
        </FaqMenuContainer>
    );
    }

const FaqMenuContainer=styled(Box)`
width: 476px;
height: 524px;
flex-shrink: 0;
border-radius: 25px;
background: #E0E1DD;
`;

const StyledTreeView=`
width: 217px;
height: 263.467px;
flex-shrink: 0;
`; 

const StyledTreeItem=styled(TreeItem2)`
color: #000;
font-family: "Open Sans";
font-size: 25px;
font-style: Bold;
font-weight: 700;
line-height: normal;
`;

export default FaqMenu;