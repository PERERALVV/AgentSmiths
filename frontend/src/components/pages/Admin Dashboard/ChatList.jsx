import React, { useEffect, useState } from "react";
import axios from "axios";
import {
  Box,
  Typography,
  Button,
  List,
  ListItem,
  ListItemText,
  CircularProgress,
  Alert,
  IconButton,
} from "@mui/material";
import { styled } from "@mui/material/styles";
import { useCookies } from "react-cookie";
import PersonIcon from "@mui/icons-material/Person";
import AndroidOutlinedIcon from "@mui/icons-material/AndroidOutlined";
import DeleteIcon from "@mui/icons-material/Delete";

const ChatHistory = styled(List)({
  overflowY: "auto",
  maxHeight: "100%",
  backgroundColor: "#f9f9f9",
  borderRadius: 8,
  padding: 16,
});

const ChatMessage = styled(ListItem)(({ theme, sender }) => ({
  display: "flex",
  alignItems: "center",
  marginBottom: theme.spacing(2),
  flexDirection: sender === "incoming" ? "row-reverse" : "row",
  "& .MuiListItemText-root": {
    maxWidth: "70%",
    padding: theme.spacing(1.5),
    borderRadius: 8,
    backgroundColor: sender === "incoming" ? "#00838f" : "#f0f0f0",
    color:
      sender === "incoming"
        ? theme.palette.common.white
        : theme.palette.text.primary,
    boxShadow: "0px 2px 4px rgba(0,0,0,0.1)",
    position: "relative",
    marginLeft: sender === "incoming" ? 0 : "auto",
    marginRight: sender === "incoming" ? "auto" : 0,
  },
  "& .sender-icon": {
    alignSelf: "flex-start",
    marginRight: theme.spacing(1),
    marginTop: theme.spacing(1),
    backgroundColor: sender === "incoming" ? "#00838f" : "#f0f0f0",
    color:
      sender === "incoming"
        ? theme.palette.common.white
        : theme.palette.text.primary,
    padding: 4,
    borderRadius: "50%",
    boxShadow: "0px 2px 4px rgba(0,0,0,0.1)",
  },
}));

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

const LeftPanel = styled(Box)({
  height: "calc(100vh - 64px)",
  width: "30%",
  paddingRight: 20,
  borderRight: "1px solid #ccc",
  overflowY: "auto",
});

const RightPanel = styled(Box)({
  height: "calc(100vh - 64px)",
  width: "70%",
  paddingLeft: 20,
  overflowY: "auto",
  backgroundColor: "#ffffff",
  padding: 20,
  boxShadow: "0 2px 4px rgba(0,0,0,0.1)",
});

const ReviewButton = styled(Button)(({ theme }) => ({
  backgroundColor: "#00838f",
  color: theme.palette.common.white,
  padding: theme.spacing(1, 3),
  borderRadius: 8,
  marginBottom: theme.spacing(2),
  boxShadow:
    "0px 3px 1px -2px rgba(0,0,0,0.2), 0px 2px 2px 0px rgba(0,0,0,0.14), 0px 1px 5px 0px rgba(0,0,0,0.12)",
  "&:hover": {
    backgroundColor: "#005662",
  },
}));

const SupportChatLayout = () => {
  const [chatHistory, setChatHistory] = useState([]);
  const [currentChat, setCurrentChat] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [cookies, setCookie, removeCookie] = useCookies(["token"]);

  useEffect(() => {
    const fetchChatHistory = async () => {
      try {
        const response = await axios.get("http://localhost:8080/support-chat", {
          headers: {
            Authorization: `Bearer ${cookies.token}`,
          },
          withCredentials: true,
        });
        setChatHistory(response.data);
        setLoading(false);
      } catch (error) {
        setError("Error fetching chat history");
        setLoading(false);
      }
    };
    if (cookies.token) {
      fetchChatHistory();
    } else {
      setLoading(false);
    }
  }, [cookies.token]);

  const handleClickOpen = (chat) => {
    setCurrentChat(chat);
  };

  const handleDeleteChat = async (chatId) => {
    console.log("Deleting chat with ID:", chatId);
    try {
      await axios.delete(`http://localhost:8080/support-chat/${chatId}`, {
        headers: {
          Authorization: `Bearer ${cookies.token}`,
        },
        withCredentials: true,
      });
      setChatHistory(chatHistory.filter((chat) => chat.id !== chatId));
      setCurrentChat(null);
    } catch (error) {
      console.error("Error deleting chat:", error);
    }
  };

  return (
    <Box height="100vh" display="flex" flexDirection="column">
      <StyledTitleTypography variant="h4">Support Chat</StyledTitleTypography>

      <Box display="flex" flex="1">
        <LeftPanel>
          {loading ? (
            <CircularProgress />
          ) : error ? (
            <Alert severity="error">{error}</Alert>
          ) : (
            chatHistory.map((chat, index) => (
              <ReviewButton key={index} onClick={() => handleClickOpen(chat)}>
                Review Chat Number {index + 1}
              </ReviewButton>
            ))
          )}
        </LeftPanel>

        <RightPanel>
          {currentChat && currentChat.chat && (
            <>
              <Typography
                variant="h6"
                gutterBottom
                style={{ marginBottom: 16 }}
              >
                Chat Details
              </Typography>
              <ChatHistory>
                {currentChat.chat.map((message, index) => (
                  <ChatMessage key={index} sender={message.direction}>
                    <ListItemText primary={message.message} />
                    <Box className="sender-icon">
                      {message.direction === "incoming" ? (
                        <PersonIcon />
                      ) : (
                        <AndroidOutlinedIcon />
                      )}
                    </Box>
                  </ChatMessage>
                ))}
              </ChatHistory>
              <IconButton
                aria-label="delete"
                onClick={() => handleDeleteChat(currentChat.id)}
                style={{
                  color: "red",
                  position: "absolute",
                  top: 90,
                  right: 30,
                }}
              >
                <DeleteIcon />
              </IconButton>
            </>
          )}
        </RightPanel>
      </Box>
    </Box>
  );
};

export default SupportChatLayout;
