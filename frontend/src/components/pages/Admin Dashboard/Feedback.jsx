import React, { useState, useEffect } from "react";
import axios from "axios";
import {
  Container,
  Typography,
  CircularProgress,
  Snackbar,
  Grid,
  Card,
  CardContent,
  CardActions,
  IconButton,
  Button,
  ThemeProvider,
} from "@mui/material";
import MuiAlert from "@mui/material/Alert";
import DeleteIcon from "@mui/icons-material/Delete";
import { useCookies } from "react-cookie";
import {
  styled,
  createTheme,
  ThemeProvider as StyledThemeProvider,
} from "@mui/material/styles";
import DOMPurify from "dompurify";

const theme = createTheme({
  palette: {
    primary: {
      main: "#0277bd", // Adjust primary color
    },
    secondary: {
      main: "#ff9800", // Adjust secondary color
    },
    error: {
      main: "#f44336", // Adjust error color
    },
    success: {
      main: "#4caf50", // Adjust success color
    },
    background: {
      default: "#f0f0f0", // Adjust default background color
    },
  },
});

const StyledTitleTypography = styled(Typography)(({ theme }) => ({
  //   backgroundColor: "#024950",
  color: "black",
  padding: theme.spacing(2),
  borderRadius: 8,
  marginBottom: theme.spacing(2),
  textAlign: "center",
  position: "sticky",
  top: 8,
  zIndex: 1100,
  fontWeight: "bold",
  fontFamily: "tahoma",
}));

const Feedback = () => {
  const [feedbacks, setFeedbacks] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [snackbarOpen, setSnackbarOpen] = useState(false);
  const [snackbarMessage, setSnackbarMessage] = useState("");
  const [updateTrigger, setUpdateTrigger] = useState(false);
  const [filter, setFilter] = useState("all"); // 'all', 'read', 'unread'

  const [cookies] = useCookies(["token"]);

  useEffect(() => {
    if (cookies.token) {
      fetchFeedbacks(cookies.token);
    } else {
      setLoading(false);
    }
  }, [cookies.token, updateTrigger]);

  const fetchFeedbacks = async (token) => {
    try {
      setLoading(true);
      const response = await axios.get("http://localhost:8080/adminfeedback", {
        headers: {
          Authorization: `Bearer ${token}`,
        },
        withCredentials: true,
      });
      setFeedbacks(response.data);
      setLoading(false);
    } catch (error) {
      console.error("Error fetching feedbacks:", error);
      setError(error.message);
      setLoading(false);
    }
  };

  const deleteFeedback = async (feedbackId) => {
    try {
      const confirmDelete = window.confirm(
        "Are you sure you want to delete this feedback?"
      );
      if (!confirmDelete) {
        return;
      }

      setLoading(true);
      await axios.delete(`http://localhost:8080/adminfeedback/${feedbackId}`, {
        headers: {
          Authorization: `Bearer ${cookies.token}`,
        },
        withCredentials: true,
      });

      const updatedFeedbacks = feedbacks.filter(
        (feedback) => feedback._id !== feedbackId
      );
      setFeedbacks(updatedFeedbacks);
      setLoading(false);
      setSnackbarMessage("Feedback deleted successfully!");
      setSnackbarOpen(true);
      setUpdateTrigger(!updateTrigger);
    } catch (error) {
      console.error("Error deleting feedback:", error);
      setError(error.message);
      setLoading(false);
    }
  };

  const markAsRead = async (feedbackId) => {
    try {
      setLoading(true);
      await axios.put(
        `http://localhost:8080/adminfeedback/${feedbackId}/update`,
        null,
        {
          headers: {
            Authorization: `Bearer ${cookies.token}`,
          },
          withCredentials: true,
        }
      );

      // Update local state to mark feedback as read
      const updatedFeedbacks = feedbacks.map((feedback) => {
        if (feedback._id === feedbackId) {
          return { ...feedback, status: "read" };
        }
        return feedback;
      });
      setFeedbacks(updatedFeedbacks);

      setLoading(false);
      setSnackbarMessage("Feedback marked as read!");
      setSnackbarOpen(true);
    } catch (error) {
      console.error("Error marking feedback as read:", error);
      setError(error.message);
      setLoading(false);
    }
  };

  const handleFilter = (filterType) => {
    setFilter(filterType);
  };

  if (loading) return <CircularProgress />;

  let filteredFeedbacks = feedbacks;
  if (filter === "read") {
    filteredFeedbacks = feedbacks.filter(
      (feedback) => feedback.status === "read"
    );
  } else if (filter === "unread") {
    filteredFeedbacks = feedbacks.filter(
      (feedback) => feedback.status === "unread"
    );
  }

  return (
    <ThemeProvider theme={theme}>
      <Container maxWidth="xl">
        <StyledTitleTypography variant="h4">Feedbacks</StyledTitleTypography>
        <div style={{ marginBottom: "16px", marginTop: "8px" }}>
          <Button
            variant="contained"
            color="primary"
            onClick={() => handleFilter("all")}
            style={{ marginRight: "8px" }}
          >
            All Messages
          </Button>
          <Button
            variant="contained"
            color="primary"
            onClick={() => handleFilter("read")}
            style={{ marginRight: "8px" }}
          >
            Read
          </Button>
          <Button
            variant="contained"
            color="primary"
            onClick={() => handleFilter("unread")}
            style={{ marginRight: "8px" }}
          >
            Unread
          </Button>
        </div>
        <div style={{ maxHeight: "82vh", overflow: "auto" }}>
          <Grid container spacing={3}>
            {filteredFeedbacks.map((feedback, index) => (
              <Grid item xs={12} key={index}>
                <Card
                  elevation={3}
                  sx={{
                    borderRadius: "12px",
                    boxShadow: "0 2px 4px rgba(0, 0, 0, 0.1)",
                    backgroundColor:
                      feedback.status === "read"
                        ? "rgba(244, 67, 54, 0.1)"
                        : "rgba(76, 175, 80, 0.1)",
                  }}
                >
                  <CardContent sx={{ padding: "16px" }}>
                    <Typography
                      variant="h6"
                      gutterBottom
                      sx={{ fontWeight: "bold", marginBottom: "8px" }}
                    >
                      {feedback.topic}
                    </Typography>
                    <Typography
                      color="textSecondary"
                      gutterBottom
                      sx={{ marginBottom: "12px" }}
                      dangerouslySetInnerHTML={{
                        __html: DOMPurify.sanitize(feedback.message),
                      }}
                    >
                      {/* {feedback.message} */}
                    </Typography>
                    <CardActions
                      sx={{ justifyContent: "flex-end", padding: 0 }}
                    >
                      {feedback.status === "unread" && (
                        <IconButton
                          color="primary"
                          onClick={() => markAsRead(feedback._id)}
                          sx={{
                            borderRadius: "20px",
                            padding: "2px 10px",
                            backgroundColor: "#4caf50",
                            "&:hover": {
                              backgroundColor: "#388e3c",
                            },
                          }}
                        >
                          <Typography
                            sx={{
                              color: "#ffffff",
                            }}
                          >
                            Done
                          </Typography>
                        </IconButton>
                      )}
                      <IconButton
                        color="error"
                        onClick={() => deleteFeedback(feedback._id)}
                        sx={{ padding: "8px" }}
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
    </ThemeProvider>
  );
};

export default Feedback;
