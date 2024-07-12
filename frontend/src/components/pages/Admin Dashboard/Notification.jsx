import React, { useEffect, useState, useRef } from "react";
import { Typography, styled } from "@mui/material";
import NotificationBox from "./notificationbox";

const NotificationsComponent = () => {
  const [notifications, setNotifications] = useState([]);
  const [newNotificationCount, setNewNotificationCount] = useState(0);
  const ws = useRef(null);

  const handleButtonClick = (action, cluster_id) => {
    if (cluster_id) {
      if (ws.current && ws.current.readyState === WebSocket.OPEN) {
        ws.current.send(JSON.stringify({ action, cluster_id }));
      }
    } else {
      console.error("Cluster ID is undefined");
    }
  };

  useEffect(() => {
    ws.current = new WebSocket("ws://localhost:8080/notifications");

    ws.current.onopen = () => {
      console.log("WebSocket connected");
    };

    ws.current.onmessage = (event) => {
      const notification = JSON.parse(event.data);
      if (notification && notification.cluster_id) {
        setNotifications((prevNotifications) => [
          ...prevNotifications,
          notification,
        ]);
        setNewNotificationCount((prevCount) => prevCount + 1);
      }
    };

    ws.current.onerror = (error) => {
      console.error("WebSocket error:", error);
    };

    ws.current.onclose = () => {
      console.log("WebSocket connection closed");
    };

    return () => {
      if (ws.current) {
        ws.current.close();
      }
    };
  }, []);

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
  }));

  return (
    <>
      <StyledTitleTypography variant="h4">Notifications</StyledTitleTypography>
      <NotificationBox
        notifications={notifications}
        newNotificationCount={newNotificationCount}
        handleButtonClick={handleButtonClick}
      />
    </>
  );
};

export default NotificationsComponent;
