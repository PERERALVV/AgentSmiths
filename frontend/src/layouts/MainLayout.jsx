import React from "react";
import { Outlet } from "react-router-dom";
import Footer from "./Footer";
import Header from "./NavBar";

const MainLayout = () => {
  return (
    <div>
      <Header />
      <Outlet />
      <Footer />
    </div>
  );
};

export default MainLayout;
