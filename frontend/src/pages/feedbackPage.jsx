import React from "react";
import Sidebar from "../components/common/Sidebar";
import Feedback from "../components/pages/Admin Dashboard/Feedback";
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

const FeedbackPage = () => {
  return (
    <Grid container spacing={0} sx={styles.root}>
      <Grid item xs={2} sx={styles.sidebar}>
        <Sidebar />
      </Grid>

      <Grid item xs={10} sx={styles.mainContent}>
        <Feedback />
      </Grid>
    </Grid>
  );
};

export default FeedbackPage;
