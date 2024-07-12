import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Typography,
  Snackbar,
  TextField,
  IconButton,
  Box,
} from "@mui/material";
import { styled } from "@mui/material/styles";
import DeleteIcon from "@mui/icons-material/Delete";
import SearchIcon from "@mui/icons-material/Search";
import MuiAlert from "@mui/material/Alert";
import { useCookies } from "react-cookie";

const StyledTableContainer = styled(TableContainer)({
  width: "100%",
  margin: "auto",
  marginTop: 20,
  boxShadow: "0 0 10px rgba(0,0,0,0.1)",
  borderRadius: 8,
  maxHeight: "calc(100vh - 200px)",
  overflowY: "auto",
});

const StyledTable = styled(Table)({
  minWidth: 650,
});

const StickyTableHead = styled(TableHead)({
  backgroundColor: "#f0f0f0",
  position: "sticky",
  top: 0,
  zIndex: 1000,
});

const StyledHeaderCell = styled(TableCell)(({ theme }) => ({
  fontWeight: "bold",
  borderBottom: "1px solid #e0e0e0",
  padding: theme.spacing(2),
}));

const StyledDataCell = styled(TableCell)(({ theme }) => ({
  borderBottom: "1px solid #e0e0e0",
  padding: theme.spacing(2),
}));

const StyledTableRow = styled(TableRow)({
  "&:nth-of-type(even)": {
    backgroundColor: "#f9f9f9",
  },
  "&:hover": {
    backgroundColor: "#f0f0f0",
  },
});

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

const ProjectList = () => {
  const [projects, setProjects] = useState([]);
  const [loading, setLoading] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState("");
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [searchProjectName, setSearchProjectName] = useState("");
  const [searchUserID, setSearchUserID] = useState("");

  const [cookies, setCookie, removeCookie] = useCookies(["token"]);

  useEffect(() => {
    if (cookies.token) {
      fetchProjects(cookies.token);
    } else {
      setLoading(false);
    }
  }, [cookies.token]);

  const fetchProjects = async () => {
    try {
      setLoading(true);
      const response = await axios.get("http://localhost:8080/projects", {
        headers: {
          Authorization: `Bearer ${cookies.token}`,
        },
        withCredentials: true,
      });
      setProjects(response.data);
      setLoading(false);
    } catch (error) {
      console.error("There was an error fetching the projects!", error);
      setLoading(false);
    }
  };

  const handleDeleteProject = async (userID) => {
    try {
      const confirmDelete = window.confirm(
        "Are you sure you want to delete this project?"
      );
      if (!confirmDelete) {
        return;
      }

      setLoading(true);
      await axios.delete(`http://localhost:8080/projects/${userID}`, {
        headers: {
          Authorization: `Bearer ${cookies.token}`,
        },
        withCredentials: true,
      });
      setSnackbarMessage("Project deleted successfully!");
      setSnackbarOpen(true);
      fetchProjects();
    } catch (error) {
      console.error(`Error deleting project with userID ${userID}:`, error);
      setLoading(false);
    }
  };

  const handleCloseSnackbar = () => {
    setSnackbarOpen(false);
  };

  const handleSearchProjectName = (event) => {
    setSearchProjectName(event.target.value);
  };

  const handleSearchUserID = (event) => {
    setSearchUserID(event.target.value);
  };

  const filteredProjects = projects.filter(
    (project) =>
      project.projectName
        .toLowerCase()
        .includes(searchProjectName.toLowerCase()) &&
      project.userID.toLowerCase().includes(searchUserID.toLowerCase())
  );

  return (
    <div className="Project-container">
      <div>
        <StyledTitleTypography variant="h4">Projects</StyledTitleTypography>
        <Box display="flex" mb={2} gap={2}>
          <TextField
            label="Search by user ID"
            variant="outlined"
            value={searchUserID}
            onChange={handleSearchUserID}
            InputProps={{
              endAdornment: (
                <IconButton>
                  <SearchIcon />
                </IconButton>
              ),
            }}
          />
          <TextField
            label="Search by project name"
            variant="outlined"
            value={searchProjectName}
            onChange={handleSearchProjectName}
            InputProps={{
              endAdornment: (
                <IconButton>
                  <SearchIcon />
                </IconButton>
              ),
            }}
          />
        </Box>
        <StyledTableContainer component={Paper}>
          <StyledTable aria-label="projects table">
            <StickyTableHead>
              <TableRow>
                <StyledHeaderCell>No</StyledHeaderCell>
                <StyledHeaderCell>User ID</StyledHeaderCell>
                <StyledHeaderCell>Project Name</StyledHeaderCell>
                <StyledHeaderCell>Delete</StyledHeaderCell>{" "}
                {/* Updated header cell */}
              </TableRow>
            </StickyTableHead>
            <TableBody>
              {filteredProjects.map((project, index) => (
                <StyledTableRow key={index}>
                  <StyledDataCell>{index + 1}</StyledDataCell>
                  <StyledDataCell>{project.userID}</StyledDataCell>
                  <StyledDataCell>{project.projectName}</StyledDataCell>
                  <StyledDataCell>
                    <DeleteIcon
                      style={{ cursor: "pointer", color: "red" }}
                      onClick={() => handleDeleteProject(project.userID)}
                    />
                  </StyledDataCell>
                </StyledTableRow>
              ))}
            </TableBody>
          </StyledTable>
        </StyledTableContainer>

        <Snackbar
          open={snackbarOpen}
          autoHideDuration={6000}
          onClose={handleCloseSnackbar}
          anchorOrigin={{ vertical: "bottom", horizontal: "left" }}
        >
          <MuiAlert
            elevation={6}
            variant="filled"
            onClose={handleCloseSnackbar}
            severity="success"
            sx={{ backgroundColor: "#43a047", color: "#fff" }}
          >
            {snackbarMessage}
          </MuiAlert>
        </Snackbar>
      </div>
    </div>
  );
};

export default ProjectList;
