import styled from "styled-components";

/*
 *
 *
 *
 *
 * ********** Show Output ***********
 *
 *
 *
 *
 */

export const ShowOutputCon = styled.div`
  width: 100%;
  min-width: 1000px;
`;

export const ShowOutputMiddle = styled.div`
  width: 100%;
  display: flex;
  justify-content: center;
  margin: 20px 0px;
`;

export const EditToolContainer = styled.div`
  width: 400px;
  height: 770px;
  margin: 0px 20px;
  border-radius: 10px;
  background-image: url("https://www.dotscastle.com/images/website-redesign.png");
  background-size: 90%;
  background-repeat: no-repeat;
  background-position: center;
  box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 2px, rgba(0, 0, 0, 0.07) 0px 2px 4px,
    rgba(0, 0, 0, 0.07) 0px 4px 8px, rgba(0, 0, 0, 0.07) 0px 8px 16px,
    rgba(0, 0, 0, 0.07) 0px 16px 32px, rgba(0, 0, 0, 0.07) 0px 32px 64px;
  display: flex;
  align-items: center;
`;

export const FormatterSectionCon = styled.div`
  margin-left: 20px;
  width: 1400px;
  height: 770px;
  flex-shrink: 0;
  background-color: rgba(120, 239, 37, 0.18);
  display: flex;
  justify-content: center;
  align-items: center;
  justify-content: center;
  box-shadow: rgba(0, 0, 0, 0.07) 0px 1px 2px, rgba(0, 0, 0, 0.07) 0px 2px 4px,
    rgba(0, 0, 0, 0.07) 0px 4px 8px, rgba(0, 0, 0, 0.07) 0px 8px 16px,
    rgba(0, 0, 0, 0.07) 0px 16px 32px, rgba(0, 0, 0, 0.07) 0px 32px 64px;
  border-radius: 5px;
`;

/*
 *
 *
 *
 *
 * *********** NavBar ***********
 *
 *
 *
 *
 */

export const NavCon = styled.div`
  width: 100%;
`;

export const ButtonCon = styled.div`
  display: flex;
  justify-content: space-evenly;
  border-radius: 25px;
  background: #e0e1dd;
  margin: 0px 20px;
`;

export const Button = styled.button`
  height: 67px;
  margin: 0;
  flex-shrink: 0;
  cursor: pointer;
  border: none;
  flex: 25%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: Inter;
  font-size: 25px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
  transition: background-color 0.2s ease-in-out;

  background-color: ${(props) => (props.active ? "#778da9" : "#e0e1dd")};
  color: ${(props) => (props.active ? "#ffffff" : "#0d1b2a")};

  &:hover {
    background-color: ${(props) => (props.active ? "#526782" : "#c9cac6")};
  }
`;

/*
 *
 *
 *
 *
 * *********** Formatter Section ***********
 *
 *
 *
 *
 */

export const GrapesEditorCon = styled.div`
  width: 100%;
  height: 100%;
  overflow: hidden;
`;

/*
 *
 *
 *
 *
 * *********** Color Editor ***********
 *
 *
 *
 *
 */

export const ColorEditorCon = styled.div`
  background: green;
`;

/*
 *
 *
 *
 *
 * *********** Font Editor ***********
 *
 *
 *
 *
 */

/*
 *
 *
 *
 *
 * *********** Text Editor ***********
 *
 *
 *
 *
 */

export const TextEditorCon = styled.div`
  background: #ffffff;
`;
/*
 *
 *
 *
 *
 * *********** Edit Tool ***********
 *
 *
 *
 *
 */

export const EditToolCon = styled.div`
  width: 400px;
  height: 600px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #ffffff;
`;

/*
 *
 *
 *
 *
 * *********** Bottom Bar ***********
 *
 *
 *
 *
 */

export const BottomBarCon = styled.div`
  width: 100%;
  height: 100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

export const BottomButton = styled.button`
  height: 50px;
  width: auto;
  padding: 0 30px;
  margin: 0 10px;
  cursor: pointer;
  border: none;
  background: #e0e1dd;
  color: #000000;
  font-family: Inter;
  font-size: 20px;
  font-style: normal;
  font-weight: 600;
  line-height: normal;
  transition: background-color 0.2s ease-in-out;
  border-radius: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  &:hover {
    background-color: #c9cac6;
`;

export const PageNavigationButton = styled.div`
  display: flex;
  justify-content: space-between;
  flex: 0.1%;
`;

export const Arrow = styled.img`
  width: 20px;
  margin-left: 20px;

  &:hover {
    transform: translateX(5px);
    transition: transform 0.2s ease-in-out;
  }
`;
