import React, { useEffect, useState } from "react";
import { Grid, Box, Typography, Paper, ButtonBase } from "@mui/material";
import { Link } from "react-router-dom";
import { styled } from "@mui/material/styles";
import PeopleIcon from "@mui/icons-material/People";
import FolderIcon from "@mui/icons-material/Folder";
import ChatIcon from "@mui/icons-material/Chat";
import NotificationsIcon from "@mui/icons-material/Notifications";
import PersonIcon from "@mui/icons-material/Person";
import FeedbackIcon from "@mui/icons-material/Feedback";
import axios from "axios";

const DashboardPage = () => {
  const [userCount, setUserCount] = useState(0);
  const [projectCount, setProjectCount] = useState(0);
  const [chatCount, setChatCount] = useState(0);
  const [feedbackCount, setFeedbackCount] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const userResponse = await axios.get(
          "http://localhost:8080/users/count"
        );
        setUserCount(userResponse.data.count);

        const projectResponse = await axios.get(
          "http://localhost:8080/projects/count"
        );
        setProjectCount(projectResponse.data.count);

        const chatResponse = await axios.get(
          "http://localhost:8080/support-chat/count"
        );
        setChatCount(chatResponse.data.count);

        const feedbackResponse = await axios.get(
          "http://localhost:8080/adminfeedback/count"
        );
        setFeedbackCount(feedbackResponse.data.count);
      } catch (error) {
        console.error("Failed to fetch data:", error);
      }
    };

    fetchData();
  }, []);

  const colorTheme = {
    background: "linear-gradient(45deg, #1e3c72, #2a5298)",
    text: "#fff",
  };

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
    backgroundColor: "#ecf0f1",
  }));

  const ShortcutBox = ({ to, title, icon, description, count }) => {
    const styles = {
      shortcutBox: {
        padding: "20px",
        margin: "10px",
        width: "calc(30% - 20px)",
        borderRadius: "12px",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        alignItems: "center",
        transition: "transform 0.3s ease, box-shadow 0.3s ease",
        backgroundImage: colorTheme.background,
        color: colorTheme.text,
        boxShadow: "0 4px 20px rgba(0, 0, 0, 0.1)",
        "&:hover": {
          transform: "scale(1.05)",
          boxShadow: "0 8px 30px rgba(0, 0, 0, 0.2)",
        },
      },
      link: {
        textDecoration: "none",
        width: "100%",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        color: colorTheme.text,
      },
      iconWrapper: {
        fontSize: "4em",
        marginBottom: "10px",
      },
      title: {
        fontSize: "1.5em",
        fontWeight: "bold",
        textTransform: "uppercase",
        marginBottom: "5px",
      },
      description: {
        fontSize: "0.9em",
        textAlign: "center",
        padding: "0 10px",
        marginBottom: "10px",
      },
      count: {
        fontSize: "2em",
        fontWeight: "bold",
        marginBottom: "10px",
      },
    };

    return (
      <Paper sx={styles.shortcutBox} elevation={3}>
        <ButtonBase
          component={Link}
          to={to}
          style={styles.link}
          focusRipple
          focusVisibleClassName="focusVisible"
        >
          <Box sx={styles.iconWrapper}>
            {React.cloneElement(icon, { style: { fontSize: "inherit" } })}
          </Box>
          <Typography variant="h6" style={styles.title}>
            {title}
          </Typography>
          {count && (
            <Typography variant="h3" style={styles.count}>
              {count}
            </Typography>
          )}
          <Typography variant="body1" style={styles.description}>
            {description}
          </Typography>
        </ButtonBase>
      </Paper>
    );
  };

  return (
    <div>
      <StyledTitleTypography variant="h4">
        Admin Dashboard
      </StyledTitleTypography>
      <Grid
        container
        spacing={3}
        justifyContent="center"
        alignItems="center"
        sx={{ height: "92vh", backgroundColor: "#ecf0f1", p: 3 }}
      >
        <Grid item xs={12}>
          <Box
            sx={{
              display: "flex",
              flexWrap: "wrap",
              justifyContent: "space-around",
            }}
          >
            <ShortcutBox
              to="/users"
              title="Users"
              icon={<PeopleIcon />}
              description={`This website has ${userCount} users`}
              count={userCount}
            />
            <ShortcutBox
              to="/projects"
              title="Projects"
              icon={<FolderIcon />}
              description={`This website has ${projectCount} projects`}
              count={projectCount}
            />
            <ShortcutBox
              to="/chatlist"
              title="Chat List"
              icon={<ChatIcon />}
              description={`This website has ${chatCount} support chat messages`}
              count={chatCount}
            />
            <ShortcutBox
              to="/notification"
              title="Notification"
              icon={<NotificationsIcon />}
              description="Manage notifications and alerts"
            />
            <ShortcutBox
              to="/adminfeedback"
              title="Feedback"
              icon={<FeedbackIcon />}
              description={`This website has ${feedbackCount} feedbacks`}
              count={feedbackCount}
            />
            <ShortcutBox
              to="/profile"
              title="Profile"
              icon={<PersonIcon />}
              description="Update your profile information"
            />
          </Box>
        </Grid>
      </Grid>
    </div>
  );
};

export default DashboardPage;
