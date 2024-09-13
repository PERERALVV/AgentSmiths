import { BrowserRouter, Route, Routes } from "react-router-dom";
import { SocketProvider } from "./SocketContext";
import MainLayout from "./layouts/MainLayout";
import ShowOutput from "./pages/ShowOutput";
import ContactUs from "./pages/ContactUs";
import Login from "./pages/login";
import Signin from "./pages/Signin";
import UserProfileView from "./pages/UserProfileView";
import forgotPassword from "./pages/emailVerification";
import otp from "./pages/otp";
import passwordChange from "./pages/changePW";
import Home from "./pages/Home";
import ChatInterface from "./pages/ChatInterface";
import StaticWebSites from "./pages/StaticWebsites";
import DashboardPage from "./pages/dashboardPage";
import UsersPage from "./pages/usersPage";
import ProjectsPage from "./pages/projectsPage";
import ChatListPage from "./pages/chatListPage";
import NotificationPage from "./pages/notificationPage";
import ProfilePage from "./pages/profilePage";
import FeedbackPage from "./pages/feedbackPage";
import Support from "./pages/Support";
import SupportAgent from "./pages/SupportAgent";

const App = () => {
  return (
    <SocketProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" Component={MainLayout}>
            <Route index Component={Home} />
            <Route path="/contactus" Component={ContactUs} />
            {/* <Route path="/showoutput" Component={ShowOutput} /> */}
            <Route path="/userprofileview" Component={UserProfileView} />
            <Route path="/passwordChange" Component={passwordChange} />
            <Route path="/chat" Component={ChatInterface} />
            <Route path="/staticwebsites" Component={StaticWebSites} />
            <Route path="/support" Component={Support} />
            <Route path="/supportagent" Component={SupportAgent} />
          </Route>
          <Route path="/showoutput" Component={ShowOutput} />
          <Route path="/login" Component={Login} />
          <Route path="/signin" Component={Signin} />
          <Route path="/fpw" Component={forgotPassword} />
          <Route path="/otp" Component={otp} />
          <Route path="/dashboard" element={<DashboardPage />} />
          <Route path="/users" element={<UsersPage />} />
          <Route path="/projects" element={<ProjectsPage />} />
          <Route path="/chatlist" element={<ChatListPage />} />
          <Route path="/notification" element={<NotificationPage />} />
          <Route path="/profile" element={<ProfilePage />} />
          <Route path="/adminfeedback" element={<FeedbackPage />} />
        </Routes>
      </BrowserRouter>
    </SocketProvider>
  );
};

export default App;
