import React from "react";
import { NavLink, useNavigate } from "react-router-dom";
import {
  Drawer,
  List,
  ListItem,
  ListItemIcon,
  ListItemText,
  Typography,
  Toolbar,
  useMediaQuery,
  useTheme,
} from "@mui/material";
import {
  Dashboard as DashboardIcon,
  People as UsersIcon,
  Folder as ProjectsIcon,
  Chat as ChatIcon,
  Notifications as NotificationsIcon,
  AccountBox as ProfileIcon,
  ExitToApp as LogoutIcon,
  Feedback as FeedbackIcon,
} from "@mui/icons-material";
import { useCookies } from "react-cookie";

const Sidebar = () => {
  const theme = useTheme();
  const isSmallScreen = useMediaQuery("(max-width:600px)");
  const isMediumScreen = useMediaQuery("(max-width:960px)");
  const isLargeScreen = useMediaQuery("(max-width:1280px)");
  const isExtraLargeScreen = useMediaQuery("(min-width:1281px)");

  let drawerWidth;
  if (isSmallScreen) {
    drawerWidth = "16.5%";
  } else if (isMediumScreen) {
    drawerWidth = "16.5%";
  } else if (isLargeScreen) {
    drawerWidth = "16.5%";
  } else if (isExtraLargeScreen) {
    drawerWidth = "16.5%";
  } else {
    drawerWidth = "16.5%";
  }

  const [cookies, setCookie, removeCookie] = useCookies(["token"]);
  const navigate = useNavigate();

  const handleLogout = async () => {
    console.log("Logout button clicked");
    try {
      const response = await fetch("http://localhost:8080/logout", {
        method: "POST",
        credentials: "include",
      });

      if (response.ok) {
        console.log("Logout successful, removing cookie");
        removeCookie("token");
        navigate("/");
      } else {
        console.error("Logout failed", response.statusText);
      }
    } catch (error) {
      console.error("An error occurred during logout", error);
    }
  };

  const menuItems = [
    {
      text: "Dashboard",
      icon: <DashboardIcon sx={{ color: "#fff" }} />,
      to: "/dashboard",
    },
    { text: "Users", icon: <UsersIcon sx={{ color: "#fff" }} />, to: "/users" },
    {
      text: "Projects",
      icon: <ProjectsIcon sx={{ color: "#fff" }} />,
      to: "/projects",
    },
    {
      text: "Support Chat",
      icon: <ChatIcon sx={{ color: "#fff" }} />,
      to: "/chatlist",
    },
    {
      text: "Feedbacks",
      icon: <FeedbackIcon sx={{ color: "#fff" }} />,
      to: "/adminfeedback",
    },
    {
      text: "Notification",
      icon: <NotificationsIcon sx={{ color: "#fff" }} />,
      to: "/notification",
    },
    {
      text: "Profile",
      icon: <ProfileIcon sx={{ color: "#fff" }} />,
      to: "/profile",
    },
    {
      text: "Logout",
      icon: <LogoutIcon sx={{ color: "#fff" }} />,
      action: handleLogout,
    },
  ];

  return (
    <Drawer
      variant="permanent"
      sx={{
        width: drawerWidth,
        flexShrink: 0,
        "& .MuiDrawer-paper": {
          width: drawerWidth,
          backgroundColor: "#024950",
        },
      }}
    >
      <Toolbar sx={{ backgroundColor: "#024950", color: "#fff" }}>
        <Typography variant="h6" sx={{ flexGrow: 1, textAlign: "center" }}>
          AgentSmiths
        </Typography>
      </Toolbar>
      <List>
        {menuItems.map(({ text, icon, to, action }) => (
          <ListItem
            key={text}
            button
            component={to ? NavLink : "div"}
            to={to}
            onClick={action}
            activeClassName={to ? "active" : undefined}
            sx={{
              borderRadius: "10px",
              mb: 1,
              height: "60px",
              "&:hover": {
                backgroundColor: "#039be5",
                color: "#fff",
              },
              "&.active": {
                backgroundColor: "#1abc9c",
                color: "#fff",
              },
            }}
          >
            <ListItemIcon>{icon}</ListItemIcon>
            <ListItemText primary={text} sx={{ color: "#fff" }} />
          </ListItem>
        ))}
      </List>
    </Drawer>
  );
};

export default Sidebar;
