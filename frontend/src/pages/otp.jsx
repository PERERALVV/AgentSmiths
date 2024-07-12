// src/components/ConfirmPasswordPage.js
import React, { useState, useRef } from "react";
import {
  Container,
  Typography,
  TextField,
  Button,
  Stack,
  Link,
} from "@mui/material";
import { makeStyles } from "@mui/styles";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import { createTheme, ThemeProvider } from "@mui/material/styles";

const useStyles = makeStyles({
  container: {
    height: "100%",
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    color: "#0D1B2A",
    padding: "40px",
    marginTop: "14%",
  },
  formContainer: {
    width: "40%",
    textAlign: "center",
    padding: "2%",
    borderRadius: "10px",
    backgroundColor: "#FFFFFF",
    boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
    marginLeft: "28%",
  },
  otpInput: {
    width: "30px",
    height: "40px",
    textAlign: "center",
    fontSize: "20px",
    border: "1px solid #ccc",
    borderRadius: "5px",
    margin: "0 5px",
    outline: "none",
    boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
  },
  signButton: {
    width: "45vh",
    height: "6vh",
    marginBottom: "0vh",
    borderRadius: "20px",
  },
});

const outerTheme = createTheme({
  palette: {
    primary: {
      dark: "#778DA9",
      main: "#0D1B2A",
    },
    secondary: {
      main: "#6070D4",
    },
  },
});

const ConfirmPasswordPage = () => {
  const classes = useStyles();
  const [otp, setOtp] = useState(Array(6).fill(""));
  const [otpError, setOtpError] = useState("");
  const navigate = useNavigate();
  const otpInputs = useRef([]);

  const handleOtpChange = (index, value) => {
    const newOtp = [...otp];
    newOtp[index] = value;
    setOtp(newOtp);

    if (index < otp.length - 1 && value !== "") {
      otpInputs.current[index + 1].focus();
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    console.log(localStorage.getItem("email"));
    const enteredOtp = otp.join("");

    if (enteredOtp.length !== 6 || !/^\d+$/.test(enteredOtp)) {
      setOtpError("Please enter a valid 6-digit OTP.");
      return;
    }

    try {
      const email = localStorage.getItem("email");
      const response = await axios.post("http://localhost:8080/otpCheck", {
        otp: enteredOtp,
        email: email,
      });

      console.log("API response:", response.data);
      navigate("/cpw"); // Navigate to Change Password page
    } catch (error) {
      console.error("Error calling API:", error);
      // Handle API call error here
    }
  };

  return (
    <Container className={classes.container}>
      <Typography
        variant="h4"
        style={{
          marginBottom: "20px",
          justifyContent: "center",
          fontWeight: "bold",
        }}
      >
        OTP Verification
      </Typography>
      <Typography
        style={{ marginTop: "-1%", justifyContent: "center", color: "#778DA9" }}
      >
        Enter the OTP sent to your email
      </Typography>
      <ThemeProvider theme={outerTheme}>
        <div className={classes.formContainer}>
          <form onSubmit={handleSubmit}>
            <Stack
              direction="row"
              spacing={2}
              justifyContent="center"
              alignItems="center"
            >
              {[0, 1, 2, 3, 4, 5].map((index) => (
                <input
                  key={index}
                  type="text"
                  maxLength={1}
                  className={classes.otpInput}
                  value={otp[index] || ""}
                  onChange={(e) => handleOtpChange(index, e.target.value)}
                  ref={(el) => (otpInputs.current[index] = el)}
                />
              ))}
            </Stack>
            {otpError && (
              <Typography
                variant="body2"
                color="error"
                style={{ marginTop: "10px" }}
              >
                {otpError}
              </Typography>
            )}
            <Button
              sx={{ borderRadius: "20px", marginTop: "4%", width: "90%" }}
              className={classes.signButton}
              variant="contained"
              color="primary"
              type="submit"
            >
              <Link
                underline="none"
                style={{ marginLeft: "5px", color: "inherit" }}
              >
                VERIFY & PROCEED
              </Link>
            </Button>
            <Typography
              style={{
                marginTop: "2%",
                justifyContent: "center",
                color: "#778DA9",
              }}
            >
              Don't receive the OTP?{" "}
              <Link href="" underline="none" sx={{ color: "#0D1B2A" }}>
                RESEND OTP
              </Link>
            </Typography>
          </form>
        </div>
      </ThemeProvider>
    </Container>
  );
};

export default ConfirmPasswordPage;
