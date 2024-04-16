import React, { useState } from 'react';
import { Typography } from '@mui/material';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';
import Checkbox from '@mui/material/Checkbox';
import FormControlLabel from '@mui/material/FormControlLabel';
import useStyle from './Lstyle';
import Stack from '@mui/material/Stack';
import { ThemeProvider, createTheme } from '@mui/material/styles';



function Login() {
    const classes = useStyle();

    const outerTheme = createTheme({
        palette: {
            primary: {
              dark: '#778DA9',
              main: '#0D1B2A'
            },
            secondary: {
                main: '#6070D4',
            },
        },
    });

    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [rememberMe, setRememberMe] = useState(false);

    const handleSubmit = (event) => {
        event.preventDefault();
        // Validate username and password
        if (username.trim() !== '' && password.trim() !== '') {
            // Add form submission logic here
        } else {
            console.error('Invalid username or password');
            alert('Invalid username or password'); // Display alert
        }
    };

    return (
        <div className='loginPage'>
            <Grid container className={classes.gridContainer}>
                <Grid item lg={6}>
                    <img src="./img/login.png" alt="Image" className={classes.loginImage} />
                </Grid>
                <Grid item alignItems='center' lg={6}>
                    <Typography marginRight={10} color='#0D1B2A' sx={{ fontWeight: 'bold' }} marginBottom={2} marginTop={6}>
                        WELCOME TO AGENTSMITH
                    </Typography>
                    <ThemeProvider theme={outerTheme}>
                        <Stack className={classes.formContainer} direction="column" spacing={0}>
                            <form onSubmit={handleSubmit}>
                                <Stack direction="column">
                                    <TextField
                                        className={classes.textField}
                                        required
                                        label="Username"
                                        value={username}
                                        onChange={(e) => setUsername(e.target.value)}
                                        InputProps={{ sx: { borderRadius: '20px' } }}
                                    />
                                    <TextField
                                        className={classes.textField}
                                        required
                                        type='password'
                                        label="Password"
                                        value={password}
                                        onChange={(e) => setPassword(e.target.value)}
                                        InputProps={{ sx: { borderRadius: '20px' } }}
                                    />
                                    <FormControlLabel
                                        control={<Checkbox
                                            checked={rememberMe}
                                            onChange={(e) => setRememberMe(e.target.checked)}
                                            color="primary"
                                        />}
                                        label="Remember Me"
                                        sx={{ color: '#778DA9'  }}
                                    />
                                    <Button sx={{ borderRadius: '20px' }} className={classes.signButton} variant="contained" color='primary' type="submit">Log In</Button>
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
