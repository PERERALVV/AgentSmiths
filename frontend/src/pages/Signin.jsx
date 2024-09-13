import React, { useState } from "react";
import { Typography } from "@mui/material";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Divider from "@mui/material/Divider";
import Button from "@mui/material/Button";
// import useStyle from '../Lstyle';
import useStyle from "../styles/pages/Lstyle";
import Stack from "@mui/material/Stack";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import Hidden from "@mui/material/Hidden";
import PersonIcon from "@mui/icons-material/Person";
import EmailIcon from "@mui/icons-material/Email";
import LockIcon from "@mui/icons-material/Lock";
import GoogleIcon from "@mui/icons-material/Google";
import FacebookIcon from "@mui/icons-material/Facebook";
import axios from "axios";

function Signin() {
  const classes = useStyle();
  const [passwordError, setPasswordError] = useState("");

  const outerTheme = createTheme({
    palette: {
      primary: {
        dark: "#778DA9",
        main: "#0D1B2A",
      },
      secondary: {
        main: "#fff",
        dark: "#0D1B2A",
      },
    },
  });

  const handleSubmit = async (event) => {
    event.preventDefault();
    const form = event.target;
    const userName = form.elements["userName"].value;
    const email = form.elements["email"].value;
    const password = form.elements["password"].value;

    // Password validation logic
    if (password.length < 8) {
      setPasswordError("Password must be at least 8 characters long.");
      return;
    } else {
      setPasswordError("");
    }

    // Make a POST request to your FastAPI endpoint
    try {
      const response = await axios.post("http://localhost:8080/signup", {
        name: userName,
        email: email,
        password: password,
      });
      console.log(response.data); // Assuming your backend returns some data
    } catch (error) {
      console.error("Error submitting form:", error);
    }
  };

  const handleGoogleLogin = () => {
    window.location.href = "http://localhost:8080/google/login";
  };

  return (
    <div className="loginPage">
      <Grid container className={classes.gridContainer}>
        <Grid item xs={12} lg={6}>
          <Hidden mdDown>
            <img
              src="./img/Login.gif"
              alt="Image"
              className={classes.loginImage}
            />
          </Hidden>
        </Grid>
        <Grid
          item
          xs={12}
          lg={6}
          className={classes.rightcon}
          sx={{ paddingLeft: "12%" }}
        >
          <Typography
            marginRight={10}
            color={"#0D1B2A"}
            sx={{ fontWeight: "bold" }}
            marginBottom={2}
            marginTop={6}
          >
            WELCOME TO AGENTSMITH
          </Typography>
          <ThemeProvider theme={outerTheme}>
            <Stack
              className={classes.formContainer}
              direction="column"
              spacing={0}
            >
              <form onSubmit={handleSubmit}>
                <Stack direction="column">
                  <TextField
                    className={classes.textField}
                    required
                    name="userName"
                    label="User Name"
                    InputProps={{
                      endAdornment: <PersonIcon fontSize="small" />,
                      sx: { borderRadius: "20px" },
                    }}
                  />
                  <TextField
                    className={classes.textField}
                    required
                    type="email"
                    name="email"
                    label="Email"
                    InputProps={{
                      endAdornment: <EmailIcon fontSize="small" />,
                      sx: { borderRadius: "20px" },
                    }}
                  />
                  <TextField
                    className={classes.textField}
                    required
                    type="password"
                    name="password"
                    label="Password"
                    error={passwordError !== ""}
                    helperText={passwordError}
                    InputProps={{
                      //   endAdornment: <LockIcon fontSize="small" />,
                      sx: { borderRadius: "20px" },
                    }}
                  />
                  <Button
                    sx={{
                      borderRadius: "20px",
                      marginTop: passwordError ? "1rem" : "0",
                    }}
                    className={classes.signButton}
                    variant="contained"
                    color="primary"
                    type="submit"
                  >
                    Sign up
                  </Button>
                </Stack>
              </form>
              <Typography
                variant="h9"
                className={classes.typo}
                marginBottom={0}
                marginTop={2}
              >
                Already have an account?{" "}
                <Link
                  href="/"
                  underline="none"
                  color="#0D1B2A"
                  sx={{ fontWeight: "bold" }}
                >
                  {" "}
                  {"Login"}{" "}
                </Link>
              </Typography>
              <br />
              <Divider className={classes.divider}> or </Divider>
              <br />
              {/* Add buttons for signing in with Facebook or Google */}
              <Stack direction="column" spacing={2}>
                <Button
                  variant="contained"
                  color="primary"
                  className={classes.signlButton}
                  startIcon={<GoogleIcon />}
                  sx={{ borderRadius: "20px" }}
                  onClick={handleGoogleLogin}
                >
                  Sign in with Google
                </Button>
                <Button
                  variant="contained"
                  color="primary"
                  className={classes.signButton}
                  startIcon={<FacebookIcon />}
                  sx={{ borderRadius: "20px" }}
                >
                  Sign in with Facebook
                </Button>
              </Stack>
              <br />
              <Typography
                variant="h9"
                className={classes.typo}
                marginBottom={0}
                marginTop={1.5}
                width="45vh"
              >
                By signing up to create an account I accept <br />
                Company’s{" "}
                <Link href="#" underline="none" color={"#0D1B2A"}>
                  {" "}
                  {"Terms of Use and Privacy Policy"}{" "}
                </Link>
              </Typography>
              <br />
            </Stack>
          </ThemeProvider>
        </Grid>
      </Grid>
    </div>
  );
}

export default Signin;
