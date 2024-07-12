import React, { useState, useEffect } from "react";
import NotificationsOutlinedIcon from "@mui/icons-material/NotificationsOutlined";
import CheckCircleOutlineIcon from "@mui/icons-material/CheckCircleOutline";
import HighlightOffIcon from "@mui/icons-material/HighlightOff";
import { Button, Box, Typography, Badge } from "@mui/material";
import { ThemeProvider, createTheme } from "@mui/material/styles";
import PropTypes from "prop-types";
import axios from "axios";

const NotificationBox = ({
  newNotificationCount,
  initialNotifications = [],
  handleButtonClick,
}) => {
  const [showNewMessages, setShowNewMessages] = useState(true);
  const [newNotifications, setNewNotifications] =
    useState(initialNotifications);
  const [oldNotifications, setOldNotifications] = useState([]);

  const outerTheme = createTheme({
    palette: {
      primary: {
        dark: "#778DA9",
        main: "#0D1B2A",
      },
      secondary: {
        main: "#FF0001",
      },
    },
  });

  const handleShowNewMessages = () => {
    setShowNewMessages(true);
  };

  const handleShowOldMessages = () => {
    setShowNewMessages(false);
  };

  const handleNotificationAction = (action, index) => {
    const updatedNewNotifications = [...newNotifications];
    const notification = updatedNewNotifications.splice(index, 1)[0];

    if (notification && notification.cluster_id) {
      const cluster_id = notification.cluster_id;
      console.log("Notification action:", action, "Cluster ID:", cluster_id);
      notification.action = action;
      setNewNotifications(updatedNewNotifications);
      setOldNotifications([...oldNotifications, notification]);
      handleButtonClick(action, cluster_id);
    } else {
      console.error("Cluster ID is undefined for notification:", notification);
    }
  };

  const renderNotifications = showNewMessages
    ? newNotifications
    : oldNotifications;

  useEffect(() => {
    const fetchNotifications = async () => {
      try {
        const response = await axios.get("/notifications");
        const allNotifications = response.data.notifications;
        const newNotifs = allNotifications.filter(
          (notification) => notification.action === "Unread"
        );
        const oldNotifs = allNotifications.filter(
          (notification) => notification.action !== "Unread"
        );
        setNewNotifications(newNotifs);
        setOldNotifications(oldNotifs);
      } catch (error) {
        console.error("Failed to fetch notifications:", error);
      }
    };

    fetchNotifications();

    const websocket = new WebSocket("ws://localhost:8080/notifications");

    websocket.onmessage = (event) => {
      const data = JSON.parse(event.data);
      console.log("WebSocket message received:", data);

      if (data.message) {
        console.log("Message:", data.message);
        return;
      }

      const { question, cluster_id } = data;
      if (question && cluster_id) {
        const newNotification = {
          question,
          date: new Date().toLocaleString(),
          cluster_id,
        };
        setNewNotifications((prev) => {
          const updatedNotifications = [...prev, newNotification];
          localStorage.setItem(
            "newNotifications",
            JSON.stringify(updatedNotifications)
          );
          return updatedNotifications;
        });
      } else {
        console.error("Received invalid WebSocket data:", data);
      }
    };

    websocket.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    websocket.onclose = () => {
      console.log("WebSocket connection closed");
    };

    return () => {
      websocket.close();
    };
  }, []);

  useEffect(() => {
    localStorage.setItem("newNotifications", JSON.stringify(newNotifications));
    localStorage.setItem("oldNotifications", JSON.stringify(oldNotifications));
  }, [newNotifications, oldNotifications]);

  return (
    <ThemeProvider theme={outerTheme}>
      <Box
        sx={{
          padding: "16px",
          border: "1px solid #ccc",
          borderRadius: "8px",
          maxWidth: "100%",
          backgroundColor: "#fff",
          boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
        }}
      >
        <Box
          sx={{ display: "flex", alignItems: "center", marginBottom: "16px" }}
        >
          <NotificationsOutlinedIcon fontSize="large" />
          <Typography variant="h6" component="h2" sx={{ marginLeft: "8px" }}>
            Notifications
          </Typography>
          {showNewMessages && newNotifications.length > 0 && (
            <Badge
              badgeContent={newNotifications.length}
              color="secondary"
              sx={{ marginLeft: "2.5%" }}
            />
          )}
        </Box>
        <Box sx={{ display: "flex", marginBottom: "16px", marginLeft: "2%" }}>
          <Button
            variant={showNewMessages ? "contained" : "outlined"}
            color="primary"
            sx={{ marginRight: "16px" }}
            onClick={handleShowNewMessages}
          >
            New Notifications
          </Button>
          <Button
            variant={!showNewMessages ? "contained" : "outlined"}
            color="primary"
            onClick={handleShowOldMessages}
          >
            Old Notifications
          </Button>
        </Box>

        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
          }}
        >
          {renderNotifications.map((notification, index) => (
            <Box
              key={index}
              sx={{
                display: "flex",
                width: "95%",
                padding: "16px",
                border: "1px solid #ccc",
                borderRadius: "8px",
                backgroundColor:
                  notification.action === "Done"
                    ? "#d4edda"
                    : notification.action === "Ignore"
                    ? "#f8d7da"
                    : "#f9f9f9",
                boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
                marginBottom: "16px",
                "&:hover": {
                  transform: notification.action ? "none" : "scale(1.05)",
                  transition: notification.action ? "none" : "transform 0.3s",
                  position: "relative",
                },
              }}
            >
              <Box
                sx={{
                  width: "8px",
                  height: "100%",
                  backgroundColor:
                    notification.action === "Done"
                      ? "#28a745"
                      : notification.action === "Ignore"
                      ? "#dc3545"
                      : "transparent",
                  marginRight: "16px",
                  borderRadius: "4px",
                }}
              />
              <Box sx={{ flexGrow: 1 }}>
                <Box
                  sx={{
                    display: "flex",
                    alignItems: "center",
                    marginBottom: "8px",
                    width: "80%",
                  }}
                >
                  {notification.action === "Done" && (
                    <CheckCircleOutlineIcon
                      sx={{ color: "#28a745", marginRight: "8px" }}
                    />
                  )}
                  {notification.action === "Ignore" && (
                    <HighlightOffIcon
                      sx={{ color: "#dc3545", marginRight: "8px" }}
                    />
                  )}
                  <Typography
                    variant="body1"
                    sx={{
                      color:
                        notification.action === "Done"
                          ? "#28a745"
                          : notification.action === "Ignore"
                          ? "#dc3545"
                          : "inherit",
                      alignContent: "center",
                    }}
                  >
                    {notification.question}
                  </Typography>
                </Box>
                {!notification.action && (
                  <Box
                    sx={{
                      display: "flex",
                      justifyContent: "flex-end",
                      marginTop: "8px",
                    }}
                  >
                    <Button
                      variant="contained"
                      color="primary"
                      sx={{ marginRight: "8px", width: "13%" }}
                      onClick={() => handleNotificationAction("Done", index)}
                    >
                      Done
                    </Button>
                    <Button
                      variant="outlined"
                      color="secondary"
                      sx={{ marginRight: "8px", width: "9%" }}
                      onClick={() => handleNotificationAction("Ignore", index)}
                    >
                      Ignore
                    </Button>
                  </Box>
                )}
              </Box>
            </Box>
          ))}
        </Box>
      </Box>
    </ThemeProvider>
  );
};

NotificationBox.propTypes = {
  initialNotifications: PropTypes.arrayOf(
    PropTypes.shape({
      question: PropTypes.string.isRequired,
      date: PropTypes.string.isRequired,
      action: PropTypes.oneOf(["Done", "Ignore"]),
      cluster_id: PropTypes.string.isRequired,
    })
  ).isRequired,
  newNotificationCount: PropTypes.number.isRequired,
  handleButtonClick: PropTypes.func.isRequired,
};

export default NotificationBox;
