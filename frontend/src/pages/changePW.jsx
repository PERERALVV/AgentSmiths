// src/components/ConfirmPasswordPage.js
import React, { useState } from 'react';
import { Container, Typography, TextField, Button, Link, Stack } from '@mui/material';
import { makeStyles } from '@mui/styles';
import LockIcon from '@mui/icons-material/Lock';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const useStyles = makeStyles({
  container: {
    height: '100%',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'center',
    alignItems: 'center',
    color: '#0D1B2A',
    padding: '40px',
    marginTop: '8%',
  },
  formContainer: {
    width: '40%',
    textAlign: 'center',
    padding: '2%',
    borderRadius: '10px',
    backgroundColor: '#FFFFFF',
    boxShadow: '0 2px 4px rgba(0, 0, 0, 0.1)',
    marginLeft: '28%',
  },
  textField: {
    marginBottom: '20px',
    '& input::placeholder': {
      color: '#ccc',
      transition: 'color 0.3s ease-in-out',
    },
    '& input:hover::placeholder': {
      color: '#0D1B2A',
    },
  },
  submitButton: {
    borderRadius: '20px',
    marginTop: '20px',
  },
  errorText: {
    color: 'red',
    marginTop: '10px',
  },
});

// const ConfirmPasswordPage = () => {
//   const classes = useStyles();
//   const navigate = useNavigate();
//   const [newPassword, setNewPassword] = useState('');
//   const [confirmPassword, setConfirmPassword] = useState('');
//   const [passwordError, setPasswordError] = useState('');

//   const handleSubmit = async (event) => {
//     event.preventDefault();
//     const email = localStorage.getItem('email');
//     if (newPassword.trim() === '' || confirmPassword.trim() === '') {
//       setPasswordError('Password cannot be empty.');
//       return;
//     }

//     if (newPassword.length < 8) {
//       setPasswordError('Password must be at least 8 characters long.');
//       return;
//     } else {
//       setPasswordError('');
//     }

//     if (newPassword !== confirmPassword) {
//       setPasswordError('Passwords do not match.');
//       return;
//     }

//     try {
//       const response = await axios.post('http://localhost:8080/passwordChange', {
//         email: email,
//         newPassword: newPassword,
//       });

//       console.log('API response:', response.data);
//       navigate('/'); // Navigate to Login page after successful password change
//     } catch (error) {
//       console.error('Error calling API:', error);
//       setPasswordError('Failed to change password. Please try again.');
//     }
//   };
const ConfirmPasswordPage = () => {
  const classes = useStyles();
  const navigate = useNavigate();
  const [oldPassword, setOldPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [passwordError, setPasswordError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    const email = localStorage.getItem('email');
    if (newPassword.trim() === '' || confirmPassword.trim() === '') {
      setPasswordError('Password cannot be empty.');
      return;
    }

    if (newPassword.length < 8) {
      setPasswordError('Password must be at least 8 characters long.');
      return;
    } else {
      setPasswordError('');
    }

    if (newPassword !== confirmPassword) {
      setPasswordError('Passwords do not match.');
      return;
    }

    try {
            const response = await axios.post('http://localhost:8080/passwordChange', {
              email: email,
              new_password: newPassword,
            });
      
            console.log('API response:', response.data);
            navigate('/'); // Navigate to Login page after successful password change
          } catch (error) {
            console.error('Error calling API:', error);
            setPasswordError('Failed to change password. Please try again.');
          }
        };
  const outerTheme = createTheme({
    palette: {
      primary: {
        dark: '#778DA9',
        main: '#0D1B2A',
      },
      secondary: {
        main: '#6070D4',
      },
    },
  });

  return (
    <Container className={classes.container}>
      <Typography variant="h4" style={{ marginBottom: '20px' }} sx={{ fontWeight: 'bold' }}>
        CHOOSE A NEW
      </Typography>
      <Typography variant="h4" style={{ marginBottom: '20px', marginTop: '-1%' }} sx={{ fontWeight: 'bold' }}>
        PASSWORD
      </Typography>
      <ThemeProvider theme={outerTheme}>
        <div className={classes.formContainer}>
          <form onSubmit={handleSubmit}>
            <Stack spacing={2}>
              <TextField
                className={classes.textField}
                required
                label="New Password"
                type="password"
                variant="outlined"
                error={passwordError !== ''}
                helperText={passwordError}
                fullWidth
                value={newPassword}
                onChange={(e) => setNewPassword(e.target.value)}
                InputProps={{
                  endAdornment: <LockIcon />,
                  sx: { borderRadius: '20px' },
                }}
              />
              <TextField
                className={classes.textField}
                required
                label="Confirm Password"
                type="password"
                variant="outlined"
                error={passwordError !== ''}
                helperText={passwordError}
                fullWidth
                value={confirmPassword}
                onChange={(e) => setConfirmPassword(e.target.value)}
                InputProps={{
                  endAdornment: <LockIcon />,
                  sx: { borderRadius: '20px' },
                }}
              />
              {passwordError && (
                <Typography variant="body2" className={classes.errorText}>
                  {passwordError}
                </Typography>
              )}
              <Button sx={{ borderRadius: '20px' }} className={classes.submitButton} variant="contained" color="primary" type="submit">
                Submit
              </Button>
            </Stack>
          </form>
          <Typography variant="body1" style={{ marginTop: '20px' }}>
            <Link href="/login" style={{ color: '#0D1B2A', textDecoration: 'none' }}>
              Back to Login
            </Link>
          </Typography>
        </div>
      </ThemeProvider>
    </Container>
  );
};

export default ConfirmPasswordPage;
