
import React, { useState, useEffect } from "react";
import axios from "axios";
import { useCookies } from "react-cookie";
import { Box, Typography, Avatar, Paper, Dialog, DialogContent, DialogTitle, Button, TextField } from "@mui/material";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { useNavigate } from 'react-router-dom';

const UserProfileView = () => {
  const navigate = useNavigate();
  const [open, setOpen] = useState(false);
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [file, setFile] = useState(null);
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    bio: "",
    address: "",
    phoneNumber: "",
    dob: "",
    profession: ""
  });
  const [cookies, setCookie, removeCookie] = useCookies(["token"]);

  useEffect(() => {
    if (cookies.token) {
      fetchUserData(cookies.token);
    } else {
      setLoading(false);
    }
  }, [cookies.token]);

  const fetchUserData = async (token) => {
    try {
      const response = await axios.get("http://localhost:8080/userDetails", {
        headers: {
          Authorization: `Bearer ${token}`
        },
        withCredentials: true
      });
      setUserData(response.data);
      setFormData({
        name: response.data.name,
        email: response.data.email,
        bio: response.data.bio || "",
        address: response.data.address || "",
        phoneNumber: response.data.phoneNumber || "",
        dob: response.data.dob || "",
        profession: response.data.profession || ""
      });
      setLoading(false);
    } catch (error) {
      console.error("Error fetching user details:", error);
      setLoading(false);
    }
  };

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
  };

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    const data = new FormData();
    data.append("name", formData.name);
    data.append("bio", formData.bio);
    data.append("address", formData.address);
    data.append("phoneNumber", formData.phoneNumber);
    data.append("dob", formData.dob);
    data.append("profession", formData.profession);
    if (file) {
      data.append("avatar", file);
    }

    try {
      const response = await axios.post(
        "http://localhost:8080/updateProfile",
        data,
        {
          headers: {
            Authorization: `Bearer ${cookies.token}`
          },
          withCredentials: true
        }
      );
      console.log("Profile updated successfully:", response.data);
      
      // Update local userData state with the updated profile data
      setUserData({
        ...userData,
        name: formData.name,
        bio: formData.bio,
        address: formData.address,
        phoneNumber: formData.phoneNumber,
        dob: formData.dob,
        profession: formData.profession,
        avatar: response.data.avatar // Assuming the response contains updated avatar path
      });
      
      handleClose();
    } catch (error) {
      console.error("Error updating profile:", error);
    }
  };

  const handleLogout = async () => {
    try {
      await axios.post("http://localhost:8080/logout", {}, { withCredentials: true });
      console.log("Logout successful");
      removeCookie("token");
      navigate('/');
    } catch (error) {
      console.error("Error logging out:", error);
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

  if (loading) {
    return <Typography>Loading...</Typography>;
  }

  return (
    <ThemeProvider theme={outerTheme}>
      <Box sx={{ position: 'relative' }}>
        {/* Top half with black background */}
        <Box
          sx={{
            backgroundColor: '#0D1B2A',
            height: '50%',
            position: 'absolute',
            top: 0,
            left: 0,
            right: 0,
            zIndex: -1,
          }}
        />
        <Typography variant="h4" gutterBottom color={'#0D1B2A'}>User Profile</Typography>
        <Paper
          elevation={3}
          sx={{
            padding: '20px',
            borderRadius: '25px',
            backgroundColor: '#fff',
            width: '90%',
            margin: 'auto',
            height: '98%',
            marginTop: '7%',
            boxShadow: '2px 2px 2px rgba(0.1, 0.1, 0.1, 0.1)',
            position: 'relative',
            overflow: 'visible'
          }}
        >
          <Box
            sx={{
              position: 'absolute',
              top: '-40px',
              left: '50%',
              height: '90%',
              transform: 'translateX(-50%)',
              zIndex: 1
            }}
          >
            <Avatar
              alt="User Avatar"
              src={userData?.avatar ? `http://localhost:8080/${userData.avatar}` : ''}
              sx={{ width: 150, height: 150, border: '4px solid white' }}
            />
          </Box>
          <Box sx={{ textAlign: 'center', height: 70, marginTop: '10%' }}>
            <Typography variant="h6">{userData?.name}</Typography>
            <Typography variant="body1">{userData?.email}</Typography>
          </Box>
          <Box marginTop="1%" sx={{textAlign:'left'}}>
            <Typography variant="h6" gutterBottom><strong>Profile Details</strong></Typography>
            <Typography variant="body1"><strong>Bio:</strong> {userData?.bio}</Typography>
            <Typography variant="body1"><strong>Address:</strong> {userData?.address}</Typography>
            <Typography variant="body1"><strong>Phone Number:</strong> {userData?.phoneNumber}</Typography>
            <Typography variant="body1"><strong>Date of Birth:</strong> {userData?.dob}</Typography>
            <Typography variant="body1"><strong>Profession:</strong> {userData?.profession}</Typography>
          </Box>
          <Box marginTop="20px" textAlign="left" sx={{ marginTop: '3%' }}>
            <Button variant="contained" color="primary" onClick={handleClickOpen} sx={{ marginRight: '15px'}}>Edit Profile</Button>
            {/* <Button variant="contained" color="secondary" onClick={handleLogout} sx={{ marginTop: '20px' }}>Logout</Button> */}
          </Box>
        </Paper>

        <Dialog open={open} onClose={handleClose}>
          <DialogTitle>Edit Profile</DialogTitle>
          <DialogContent>
            <form onSubmit={handleSubmit} style={{ minWidth: 300 }}>
              <TextField
                margin="dense"
                name="name"
                label="Name"
                type="text"
                fullWidth
                value={formData.name}
                onChange={handleInputChange}
                required
              />
              <TextField
                margin="dense"
                name="email"
                label="Email"
                type="email"
                fullWidth
                value={formData.email}
                onChange={handleInputChange}
                disabled // Disable input
                required
              />
              <TextField
                margin="dense"
                name="bio"
                label="Bio"
                type="text"
                fullWidth
                value={formData.bio}
                onChange={handleInputChange}
              />
              <TextField
                margin="dense"
                name="address"
                label="Address"
                type="text"
                fullWidth
                value={formData.address}
                onChange={handleInputChange}
              />
              <TextField
                margin="dense"
                name="phoneNumber"
                label="Phone Number"
                type="text"
                fullWidth
                value={formData.phoneNumber}
                onChange={handleInputChange}
              />
              <TextField
                margin="dense"
                name="dob"
                label="Date of Birth"
                type="date"
                fullWidth
                value={formData.dob}
                onChange={handleInputChange}
                InputLabelProps={{
                  shrink: true,
                }}
              />
              <TextField
                margin="dense"
                name="profession"
                label="Profession"
                type="text"
                fullWidth
                value={formData.profession}
                onChange={handleInputChange}
              />
              <input type="file" onChange={handleFileChange} style={{ marginTop: '10px' }} />
              <Box marginTop="20px">
                <Button variant="contained" color="primary" type="submit" sx={{ marginRight: '10px' }}>Save</Button>
                <Button variant="contained" onClick={handleClose}>Cancel</Button>
              </Box>
            </form>
          </DialogContent>
        </Dialog>
      </Box>
    </ThemeProvider>
  );
};

export default UserProfileView;
