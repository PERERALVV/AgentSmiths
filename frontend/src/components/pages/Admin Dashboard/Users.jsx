import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Container,
  Typography,
  TextField,
  Button,
  CircularProgress,
  Snackbar,
  Grid,
  Card,
  CardContent,
  CardActions,
  IconButton,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Alert,
  Select,
  MenuItem,
} from "@mui/material";
import MuiAlert from "@mui/material/Alert";
import SearchIcon from "@mui/icons-material/Search";
import EditIcon from "@mui/icons-material/Edit";
import DeleteIcon from "@mui/icons-material/Delete";
import SaveIcon from "@mui/icons-material/Save";
import CancelIcon from "@mui/icons-material/Cancel";
import { useCookies } from "react-cookie";
import { styled } from "@mui/material/styles";

const StyledTitleTypography = styled(Typography)(({ theme }) => ({
  fontWeight: "bold",
  fontFamily: "tahoma",
  color: "black",
  padding: theme.spacing(2),
  borderRadius: 8,
  marginBottom: theme.spacing(2),
  textAlign: "center",
  position: "sticky",
  top: 8,
  zIndex: 1100,
  marginTop: theme.spacing(1),
}));

const Users = () => {
  const [users, setUsers] = useState([]);
  const [editingUser, setEditingUser] = useState(null);
  const [updatedUser, setUpdatedUser] = useState({});
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [searchQuery, setSearchQuery] = useState("");
  const [filteredUsers, setFilteredUsers] = useState([]);
  const [openDialog, setOpenDialog] = useState(false);
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState("");
  const [updateTrigger, setUpdateTrigger] = useState(false);

  const [cookies] = useCookies(["token"]);

  useEffect(() => {
    if (cookies.token) {
      fetchUsers(cookies.token);
    } else {
      setLoading(false);
    }
  }, [cookies.token]);

  const fetchUsers = async () => {
    try {
      setLoading(true);
      const response = await axios.get("http://localhost:8080/users", {
        headers: {
          Authorization: `Bearer ${cookies.token}`,
        },
        withCredentials: true,
      });
      setUsers(response.data);
      setLoading(false);
    } catch (error) {
      console.error("Error fetching users:", error);
      setError(error.message);
      setLoading(false);
    }
  };

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setUpdatedUser({ ...updatedUser, [name]: value });
  };

  const editUser = (user) => {
    setEditingUser(user);
    setUpdatedUser({ ...user });
    setOpenDialog(true);
  };

  const updateUser = async () => {
    try {
      setLoading(true);
      const isModified = Object.keys(updatedUser).some(
        (key) => updatedUser[key] !== editingUser[key]
      );
      if (!isModified) {
        setLoading(false);
        setOpenDialog(false);
        return;
      }

      const response = await axios.put(
        `http://localhost:8080/users/${editingUser.id}`,
        updatedUser,
        {
          headers: {
            Authorization: `Bearer ${cookies.token}`,
          },
          withCredentials: true,
        }
      );

      const updatedUserData = response.data;
      const updatedUsers = users.map((user) =>
        user.id === updatedUserData.id ? updatedUserData : user
      );
      setUsers(updatedUsers);
      setEditingUser(null);
      setOpenDialog(false);
      setLoading(false);
      setSnackbarMessage("User updated successfully!");
      setSnackbarOpen(true);
      setUpdateTrigger(!updateTrigger);
      fetchUsers();
    } catch (error) {
      console.error("Error updating user:", error);
      setError(error.message);
      setLoading(false);
    }
  };

  const deleteUser = async (userId) => {
    try {
      const confirmDelete = window.confirm(
        "Are you sure you want to delete this user?"
      );
      if (!confirmDelete) {
        return;
      }

      setLoading(true);
      await axios.delete(`http://localhost:8080/users/${userId}`, {
        headers: {
          Authorization: `Bearer ${cookies.token}`,
        },
        withCredentials: true,
      });

      const updatedUsers = users.filter((user) => user.id !== userId);
      setUsers(updatedUsers);
      setLoading(false);
      setSnackbarMessage("User deleted successfully!");
      setSnackbarOpen(true);
      setUpdateTrigger(!updateTrigger);
    } catch (error) {
      console.error("Error deleting user:", error);
      setError(error.message);
      setLoading(false);
    }
  };

  const handleSearch = (e) => {
    const query = e.target.value.toLowerCase();
    setSearchQuery(query);
    const filteredUsers = users.filter((user) => {
      const fullName = `${user.name}`.toLowerCase();
      return fullName.includes(query);
    });
    setFilteredUsers(filteredUsers);
  };

  const usersToDisplay = searchQuery ? filteredUsers : users;

  if (loading) return <CircularProgress />;
  if (error) return <Alert severity="error">{error}</Alert>;

  return (
    <Container maxWidth="xl">
      <StyledTitleTypography variant="h4">Users</StyledTitleTypography>
      <TextField
        fullWidth
        label="Search by name"
        variant="outlined"
        value={searchQuery}
        onChange={handleSearch}
        style={{ marginBottom: "1rem" }}
        InputProps={{
          endAdornment: (
            <IconButton>
              <SearchIcon />
            </IconButton>
          ),
        }}
      />
      <div style={{ maxHeight: "78vh", overflow: "auto" }}>
        <Grid container spacing={3}>
          {usersToDisplay.map((user) => (
            <Grid item xs={12} key={user.id}>
              <Card elevation={3}>
                <CardContent>
                  <Typography variant="h6" gutterBottom>
                    {user.name}
                  </Typography>
                  <Typography color="textSecondary" gutterBottom>
                    <strong>Email:</strong> {user.email}
                  </Typography>
                  <Typography color="textSecondary" gutterBottom>
                    <strong>User role:</strong> {user.role}
                  </Typography>
                  {user.bio && (
                    <Typography color="textSecondary" gutterBottom>
                      <strong>Bio:</strong> {user.bio}
                    </Typography>
                  )}
                  {user.address && (
                    <Typography color="textSecondary" gutterBottom>
                      <strong>Address:</strong> {user.address}
                    </Typography>
                  )}
                  {user.phoneNumber && (
                    <Typography color="textSecondary" gutterBottom>
                      <strong>PhoneNumber:</strong> {user.phoneNumber}
                    </Typography>
                  )}
                  {user.dob && (
                    <Typography color="textSecondary" gutterBottom>
                      <strong>Date of Birth:</strong> {user.dob}
                    </Typography>
                  )}
                  {user.profession && (
                    <Typography color="textSecondary" gutterBottom>
                      <strong>Profession:</strong> {user.profession}
                    </Typography>
                  )}
                  <CardActions>
                    <IconButton color="primary" onClick={() => editUser(user)}>
                      <EditIcon />
                    </IconButton>
                    <IconButton
                      color="error"
                      onClick={() => deleteUser(user.id)}
                    >
                      <DeleteIcon />
                    </IconButton>
                  </CardActions>
                </CardContent>
              </Card>
            </Grid>
          ))}
        </Grid>
      </div>
      <Dialog
        open={openDialog}
        onClose={() => setOpenDialog(false)}
        BackdropProps={{
          style: { backgroundColor: "rgba(0, 0, 0, 0.5)" },
        }}
      >
        <DialogTitle>Edit User Role</DialogTitle>
        <DialogContent>
          <Select
            fullWidth
            label="User role"
            name="role"
            value={updatedUser.role || ""}
            onChange={handleInputChange}
            margin="normal"
            variant="outlined"
            style={{ marginBottom: "1rem" }}
          >
            <MenuItem value="user">User</MenuItem>
            <MenuItem value="admin">Admin</MenuItem>
            <MenuItem value="supportAgent">Support-Agent</MenuItem>
          </Select>
        </DialogContent>
        <DialogActions>
          <Button
            variant="contained"
            color="primary"
            startIcon={<SaveIcon />}
            onClick={updateUser}
          >
            Save
          </Button>
          <Button
            variant="outlined"
            color="secondary"
            startIcon={<CancelIcon />}
            onClick={() => setOpenDialog(false)}
          >
            Cancel
          </Button>
        </DialogActions>
      </Dialog>
      <Snackbar
        open={snackbarOpen}
        autoHideDuration={4000}
        onClose={() => setSnackbarOpen(false)}
        anchorOrigin={{ vertical: "bottom", horizontal: "left" }}
        SnackbarContentProps={{
          style: { backgroundColor: "rgba(0, 150, 136, 0.8)" },
        }}
      >
        <MuiAlert
          elevation={6}
          variant="filled"
          onClose={() => setSnackbarOpen(false)}
          severity="success"
        >
          {snackbarMessage}
        </MuiAlert>
      </Snackbar>
    </Container>
  );
};

export default Users;
