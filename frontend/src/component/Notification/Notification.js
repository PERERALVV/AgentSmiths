import React, { useState, useEffect } from 'react';
import { IconButton, Badge, Popover, List, ListItem, ListItemText } from '@mui/material';
import { Notifications as NotificationsIcon } from '@mui/icons-material';

function NotificationBell() {
  const [notifications, setNotifications] = useState([]);
  const [anchorEl, setAnchorEl] = useState(null);

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const handleNotificationClick = () => {
    // Handle notification click here
    handleClose();
  };

  const fetchNotifications = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/analyze_chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ chat_text: 'Your chat text here' }), // Pass your chat text here
      });
      if (!response.ok) {
        throw new Error('Failed to fetch notifications');
      }
      const data = await response.json();
      setNotifications([data.conclusion]); // Assuming the conclusion is the notification
    } catch (error) {
      console.error(error);
    }
  };
  

  useEffect(() => {
    fetchNotifications();
  }, []); // Fetch notifications when the component mounts

  const renderNotifications = () => {
    return (
      <Popover
        open={Boolean(anchorEl)}
        anchorEl={anchorEl}
        onClose={handleClose}
        anchorOrigin={{
          vertical: 'bottom',
          horizontal: 'right',
        }}
        transformOrigin={{
          vertical: 'top',
          horizontal: 'right',
        }}
      >
        <List>
          {notifications.map((notification, index) => (
            <ListItem button key={index} onClick={handleNotificationClick}>
              <ListItemText primary={notification} />
            </ListItem>
          ))}
        </List>
      </Popover>
    );
  };

  return (
    <div>
      <IconButton color="inherit" onClick={handleClick}>
        <Badge badgeContent={notifications.length} color="error">
          <NotificationsIcon />
        </Badge>
      </IconButton>
      {renderNotifications()}
    </div>
  );
}

export default NotificationBell;
