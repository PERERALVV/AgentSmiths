import './App.css';
import { BrowserRouter as Router, Route,Routes, Switch, BrowserRouter } from 'react-router-dom';
import Login from './component/Login/login';
import Signin from './component/Signup/Signin';
import UserProfileView from './component/userProfile/UserProfileView';
import Fpw from './component/fogetPassword/emailVerification';
import OTPVerification from './component/fogetPassword/otp';
// import Notifications from './component/Notification/Notifications';
import ConfirmPasswordPage from './component/fogetPassword/changePW';
// import NotificationBell from './component/Notification/Notification';
// import Projects from './component/Projects/Projects';

function App() {
  return (
      <div className="App">
      <Router>
      <Routes>
            <Route exact path="/userprofile" element={<UserProfileView/>} />
            <Route path="/" element={<Login/>} />
            <Route path="/signin" element={<Signin/>} />
            <Route path="/fpw" element={<Fpw/>} />
            <Route path="/otp" element={<OTPVerification/>}/>
            <Route path="/cpw" element={<ConfirmPasswordPage/>}/>
            {/* <Route path="/notifications" element={<NotificationBell/>} /> */}
            
            {/* <Route path="/pjct" element={<Projects/>} /> */}

      </Routes>
      </Router>
      </div>

  );
}

export default App;