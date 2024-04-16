
// Import necessary components and styles
import React from 'react';
import { Typography } from '@mui/material';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Link from '@mui/material/Link';
import Divider from '@mui/material/Divider';
import Button from '@mui/material/Button';
import useStyle from './Lstyle';
import Stack from '@mui/material/Stack';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import { Link as RouterLink } from 'react-router-dom';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';

function Signin() {
    const classes = useStyle();

    const outerTheme = createTheme({
        palette: {
            primary: {
              dark: '#778DA9',
                main: '#0D1B2A'
            },
            secondary: {
                main: '#fff',
                dark: '#0D1B2A',
              
            }
        },
    });

    const handleSubmit = (event) => {
        event.preventDefault();
        // Add form submission logic here
    };

    return (
        
        <div className='loginPage'>
            <Grid container className={classes.gridContainer}>
                <Grid item lg={6}>
                    <img src="./img/login.png" alt="Image" className={classes.loginImage} />
                </Grid>
                <Grid item alignItems='center' lg={6}>
                    <Typography  marginRight={10} color={'#0D1B2A'} sx={{ fontWeight: 'bold' }} marginBottom={2} marginTop={6} >
                       WELCOME TO AGENTSMITH
                    </Typography>
                    <ThemeProvider theme={outerTheme}>
                        <Stack className={classes.formContainer} direction="column" spacing={0}>
                            <form onSubmit={handleSubmit}>
                                <Stack direction="column">
                                    <TextField
                                        className={classes.textField}
                                        required
                                        label="User Name"
                                        InputProps={{ sx: { borderRadius: '20px' } }}
                                    />
                                    <TextField
                                        className={classes.textField}
                                        required
                                        type='email'
                                        label="Email"
                                        InputProps={{ sx: { borderRadius: '20px' } }}
                                    />
                                    <TextField
                                        className={classes.textField}
                                        required
                                        type='password'
                                        label="Password"
                                        InputProps={{ sx: { borderRadius: '20px' } }}
                                    />
                                    <Button sx={{ borderRadius: '20px' }} className={classes.signButton} variant="contained" color='primary'>Sign up</Button>
                                </Stack>
                            </form>
                            <Typography variant='h9' className={classes.typo} marginBottom={0} marginTop={2}>
                                Already have an account? <Link href="#" underline="none" color='#0D1B2A'sx={{ fontWeight: 'bold' }}> {'Login'} </Link>
                            </Typography>
                            <br />
                            <Divider className={classes.divider}> or </Divider>
                            <br />
                            {/* Add buttons for signing in with Facebook or Google */}
                            <Stack direction="column" spacing={2}>
                                <Button variant="contained" color="primary" className={classes.signlButton} sx={{ borderRadius: '20px' }}>Google Account</Button>
                                <Button variant="contained" color="primary" className={classes.signButton} sx={{ borderRadius: '20px' }}>Facebook Account</Button>
                            </Stack>
                            <br />
                            <Typography variant='h9' className={classes.typo} marginBottom={0} marginTop={1.5} width='45vh'>
                                By signing up to create an account I accept <br />Company’s <Link href="#" underline="none" color={'#0D1B2A'}> {'Terms of Use and Privacy Policy'} </Link>
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