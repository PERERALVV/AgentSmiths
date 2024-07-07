import React, { useState, useEffect } from "react";
import { Typography } from "@mui/material";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import Link from "@mui/material/Link";
import Button from "@mui/material/Button";
import Checkbox from "@mui/material/Checkbox";
import FormControlLabel from "@mui/material/FormControlLabel";
import Stack from "@mui/material/Stack";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import PersonIcon from "@mui/icons-material/Person";
import Hidden from "@mui/material/Hidden";
import axios from "axios";
import { useNavigate } from "react-router-dom";
import Cookies from "js-cookie";
import useStyle from "../styles/pages/Lstyle";

const ACCESS_TOKEN_EXPIRE_MINUTES = 30;

function Login() {
  const navigate = useNavigate();
  const classes = useStyle();

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

  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [rememberMe, setRememberMe] = useState(false);
  const [passwordError, setPasswordError] = useState("");

  const clearExistingToken = () => {
    document.cookie.split(";").forEach((cookie) => {
      if (cookie.trim().startsWith("token=")) {
        document.cookie = `${
          cookie.split("=")[0]
        }=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
      }
    });
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (username.trim() !== "" && password.trim() !== "") {
      if (password.length < 8) {
        setPasswordError("Password must be at least 8 characters long.");
        return;
      } else {
        setPasswordError("");
      }

      try {
        const response = await axios.post("http://localhost:8080/login", {
          name: username,
          password: password,
        });

        console.log(response.data.access_token);

        if (response.data.access_token) {
          const token = response.data.access_token;
          Cookies.set("token", token, {
            expires: ACCESS_TOKEN_EXPIRE_MINUTES / (24 * 60),
          });

          // Assuming the backend decodes the token and sends back the role
          const role = response.data.role;

          console.log(response);
          if (role === "user") {
            navigate("/userprofileview");
          } else if (role === "admin") {
            navigate("/dashboard");
          } else if (role === "supportAgent") {
            navigate("/supportagent"); //////////////
          } else {
            console.error("Unknown role:", role);
            alert("Unknown role. Please contact support.");
          }
        } else {
          console.error("Login failed");
          alert("Login failed");
        }
      } catch (error) {
        console.error("Error submitting form:", error);
        alert("Error submitting form. Please try again.");
      }
    } else {
      console.error("Invalid username or password");
      alert("Invalid username or password");
    }
  };

  return (
    <div className="loginPage">
      <Grid container className={classes.gridContainer}>
        <Hidden mdDown>
          <Grid item lg={6} className={classes.imageContainer}>
            <img
              src="./img/Login.gif"
              alt="Image"
              className={classes.loginImage}
              height={"80%"}
              width={"45%"}
            />
          </Grid>
        </Hidden>
        <Grid item alignItems="center" lg={6} sx={{ paddingLeft: "12%" }}>
          <Typography
            marginRight={10}
            color="#0D1B2A"
            sx={{ fontWeight: "bold" }}
            marginBottom={2}
            marginTop={1}
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
                    label="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    InputProps={{
                      endAdornment: <PersonIcon fontSize="small" />,
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
                    onChange={(e) => setPassword(e.target.value)}
                    InputProps={{
                      sx: { borderRadius: "20px" },
                    }}
                  />
                  <Stack
                    direction="row"
                    justifyContent="space-between"
                    alignItems="center"
                    marginBottom="8px"
                  >
                    <FormControlLabel
                      control={
                        <Checkbox
                          checked={rememberMe}
                          onChange={(e) => setRememberMe(e.target.checked)}
                          color="primary"
                        />
                      }
                      label="Remember Me"
                      sx={{ color: "#778DA9", fontSize: "10px" }}
                    />
                    <Typography
                      variant="body1"
                      sx={{ textAlign: "right", color: "#778DA9" }}
                    >
                      <Link
                        href="/fpw"
                        underline="none"
                        sx={{ color: "#778DA9" }}
                      >
                        Forgot Password?
                      </Link>
                    </Typography>
                  </Stack>
                  <Button
                    sx={{ borderRadius: "20px" }}
                    className={classes.signButton}
                    variant="contained"
                    color="primary"
                    type="submit"
                  >
                    Log In
                  </Button>
                  <Typography
                    variant="body1"
                    sx={{ textAlign: "center", marginTop: 2, color: "#778DA9" }}
                  >
                    Not registered?{" "}
                    <Link
                      href="/signin"
                      underline="none"
                      sx={{ color: "#0D1B2A" }}
                    >
                      Create an account
                    </Link>
                  </Typography>
                </Stack>
              </form>
            </Stack>
          </ThemeProvider>
        </Grid>
      </Grid>
    </div>
  );
}

export default Login;
