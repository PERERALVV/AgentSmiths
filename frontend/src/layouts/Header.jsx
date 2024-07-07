import { useState } from "react";
//import DehazeIcon from "@mui/icons-material/Dehaze";
// import {
//   HeaderMainCon,
//   LogoImage,
//   MobileMenuButton,
//   StyledLinkM,
// } from "../styles/layout/header";

const Header = () => {
  const [open, setOpen] = useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    // <HeaderMainCon>
    //   <StyledLinkM to="/">
    //     <LogoImage src={Logo} alt="logo" />
    //   </StyledLinkM>
    //   <MobileMenuButton onClick={handleOpen}>
    //     <DehazeIcon fontSize="large" />
    //   </MobileMenuButton>
    //   <MobileMenu open={open} handleClose={handleClose} />
    // </HeaderMainCon>
    <div
      style={{
        height: "50px",
        backgroundColor: "orange",
        textAlign: "center",
        fontSize: "20px",
      }}
    >
      header
    </div>
  );
};

export default Header;
