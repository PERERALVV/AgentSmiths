// src/components/ForgotPasswordPage.js
import React, { useState } from "react";
import {
  makeStyles,
  Container,
  Typography,
  Grid,
  TextField,
  Button,
  Snackbar,
  ThemeProvider,
  createTheme,
} from "@material-ui/core";
import MuiAlert from "@material-ui/lab/Alert";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import useStyles from "../styles/pages/Lstyle";

const theme = createTheme({
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

const ForgotPasswordPage = () => {
  const classes = useStyles();
  const [email, setEmail] = useState("");
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const navigate = useNavigate();

  const handleEmailChange = (event) => {
    setEmail(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    localStorage.setItem("email", email);
    try {
      const response = await axios.post("http://localhost:8080/emailCheck", {
        email: email,
      });

      if (response.data) {
        setSnackbarOpen(true); // Show success snackbar
        setTimeout(() => {
          navigate("/otp"); // Navigate to OTP verification page
        }, 1000); // Slight delay to allow snackbar to show
      } else {
        console.error("Reset password request failed:", response.data.error);
      }
    } catch (error) {
      console.error("Error sending reset password request:", error);
    }
  };

  const handleCloseSnackbar = () => {
    setSnackbarOpen(false);
  };

  return (
    <ThemeProvider theme={theme}>
      <Container component="main" maxWidth="md" className={classes.container}>
        <Grid
          container
          spacing={0}
          direction="column"
          alignItems="center"
          justify="center"
          style={{ minHeight: "100vh" }}
        >
          <Grid item xs={12} sm={8}>
            <div className={classes.formContainer}>
              <Typography component="h1" variant="h4" gutterBottom>
                Forgot Password
              </Typography>
              <Typography variant="body2" className={classes.smallText}>
                Enter the email address associated with your account
              </Typography>
              <form onSubmit={handleSubmit} style={{ width: "100%" }}>
                <TextField
                  variant="outlined"
                  required
                  fullWidth
                  id="email"
                  label="Email Address"
                  name="email"
                  autoComplete="email"
                  value={email}
                  onChange={handleEmailChange}
                  margin="normal"
                  InputProps={{
                    sx: { borderRadius: "20px" },
                  }}
                />
                <Button
                  type="submit"
                  fullWidth
                  variant="contained"
                  color="primary"
                  sx={{ borderRadius: "20px", marginTop: "1rem" }}
                >
                  Send Reset Email
                </Button>
              </form>
            </div>
          </Grid>
        </Grid>
      </Container>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={6000}
        onClose={handleCloseSnackbar}
      >
        <MuiAlert
          elevation={6}
          variant="filled"
          onClose={handleCloseSnackbar}
          severity="success"
        >
          Reset password email sent.
        </MuiAlert>
      </Snackbar>
    </ThemeProvider>
  );
};

export default ForgotPasswordPage;
