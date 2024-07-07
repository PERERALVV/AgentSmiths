import React from "react";
import Sidebar from "../components/common/Sidebar";
import Notification from "../components/pages/Admin Dashboard/Notification";
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

const NotificationPage = () => {
  return (
    <Grid container spacing={2} sx={styles.root}>
      <Grid item xs={2} sx={styles.sidebar}>
        <Sidebar />
      </Grid>

      <Grid item xs={10} sx={styles.mainContent}>
        <Notification />
      </Grid>
    </Grid>
  );
};

export default NotificationPage;
