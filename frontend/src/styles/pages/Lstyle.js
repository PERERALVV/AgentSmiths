import { makeStyles } from "@mui/styles";
//import { ThemeProvider, createTheme }from '@mui/material/styles';

const useStyle = makeStyles((theme) => ({
  gridContainer: {
    alignItems: "center",
    spacing: "0",
    height: "100vh",
    background: "#fff",
  },
  formContainer: {
    // marginRight: '60%'
    alignItems: "center",
    justifyItems: "center",
    height: "100%",
    marginLeft: "-15%",
    // marginTop:'20%'
    //spacing:'30px'
  },
  textField: {
    width: "45vh",
    height: "10vh",
    marginBottom: "0px",
    "& .MuiInputLabel-root": {
      color: "#0D1B2A", // Styles the label
    },
    "& .MuiOutlinedInput-root": {
      "& fieldset": {
        borderColor: "#0D1B2A", // Styles the input border
      },
      "&:hover fieldset": {
        borderColor: "#0D1B2A", // Styles the input border on hover
      },
    },
  },

  loginImage: {
    width: "70%",
    height: "60%",
  },

  signButton: {
    width: "45vh",
    height: "6vh",
    marginBottom: "0vh",
    borderRadius: "20px",
  },
  divider: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    width: "45vh",
    color: "#0D1B2A",
    paddingBottom: "0",
    marginTop: "1px",
    marginBottom: "0px",
    margin: "0",
    "&.MuiDivider-root": {
      "&::before": {
        borderTop: "thin solid '#0D1B2A'",
      },
      "&::after": {
        borderTop: "thin solid '#0D1B2A'",
      },
    },
  },
  typo: {
    fontSize: "13.6px",
    color: "#778DA9",
  },

  rightColumn: {
    // display: 'flex',
    justifyContent: "center",
    // alignItems: 'center',
    //marginLeft: '15cm', // Adjust this value as needed
  },
}));

export default useStyle;
