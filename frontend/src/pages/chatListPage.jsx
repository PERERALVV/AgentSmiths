import React from "react";
import Sidebar from "../components/common/Sidebar";
import ChatList from "../components/pages/Admin Dashboard/ChatList";
import { Grid } from "@mui/material";

const styles = {
  root: {
    height: "100vh",
  },
  sidebar: {
    height: "100%",
  },
  mainContent: {
    height: "100%",
    overflowY: "auto",
  },
};

const SupportChatPage = () => {
  return (
    <Grid container spacing={2} sx={styles.root}>
      <Grid item xs={2} sx={styles.sidebar}>
        <Sidebar />
      </Grid>

      <Grid item xs={10} sx={styles.mainContent}>
        <ChatList />
      </Grid>
    </Grid>
  );
};

export default SupportChatPage;
