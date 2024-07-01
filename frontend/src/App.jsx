import React from 'react';
import {Route, Routes, BrowserRouter} from 'react-router-dom';
import Home from './pages/Home';
import SupportPage from './pages/Support';
import ServicePlansPage from './pages/ServicePlans';
import ContactPage from './pages/Contact';
import ChatInterface from './pages/ChatInterface';
import LogInPage from './pages/LogIn';
import DemoPage from './pages/DemoPage';
import StaticWebsites from './pages/StaticWebsites';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home/>} />
        <Route path="/Support" element={<SupportPage/>} />
        <Route path="/ServicePlans" element={<ServicePlansPage/>} />
        <Route path="/ContactUs" element={<ContactPage/>} />
        <Route path="/GetStarted" element={<ChatInterface />} />
        <Route path="/StaticWebsites" element={<StaticWebsites/>} />
        <Route path="/LogIn" element={<LogInPage/>} />
        <Route path="/Demo" element={<DemoPage/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
