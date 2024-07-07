import React from "react";
import Sidebar from "../components/common/Sidebar";
import Dashboard from "../components/pages/Admin Dashboard/Dashboard";
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

const DashboardPage = () => {
  return (
    <Grid container spacing={0} sx={styles.root}>
      <Grid item xs={2} sx={styles.sidebar}>
        <Sidebar />
      </Grid>

      <Grid item xs={10} sx={styles.mainContent}>
        <Dashboard />
      </Grid>
    </Grid>
  );
};

export default DashboardPage;
