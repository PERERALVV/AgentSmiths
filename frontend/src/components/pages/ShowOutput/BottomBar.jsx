import React from "react";
import {
  BottomBarCon,
  BottomButton,
  PageNavigationButton,
  Arrow,
} from "../../../styles/pages/ShowOutput";

const BottomBar = () => {
  return (
    <BottomBarCon>
      <PageNavigationButton>
        <BottomButton>{"<<"} Previous web page</BottomButton>
        <BottomButton>Next web page {">>"}</BottomButton>
      </PageNavigationButton>
      <BottomButton
        style={{
          boxShadow:
            "rgba(50, 50, 93, 0.25) 0px 30px 60px -12px inset, rgba(0, 0, 0, 0.3) 0px 18px 36px -18px inset",
        }}
      >
        Generate Website
        <div
          style={{
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
          }}
        >
          <Arrow
            src="https://images.vexels.com/media/users/3/136987/isolated/preview/7fbb17ce79710b1d578b02cc02da8592-thin-right-arrowhead.png"
            alt="arrow"
          />
        </div>
      </BottomButton>
    </BottomBarCon>
  );
};

export default BottomBar;
