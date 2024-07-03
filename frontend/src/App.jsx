import { BrowserRouter, Route, Routes } from "react-router-dom";
// import MainLayout from "./layouts/MainLayout";
// import Home from "./pages/Home";
// import ShowOutput from "./pages/ShowOutput";
// import SupportAgentPage from "./pages/SupportAgent";
// import SupportBot from "./components/pages/Support/supportbot";
// import FaqItem from "./components/pages/Support/faqitem";
// import FaqMenu from "./components/pages/Support/faqmenu";
// import ChatbotButton from "./components/pages/Support/chatbotButton";
// import ChatList from "./components/pages/supportAgent/ConvoList";
// import Actions from "./components/pages/supportAgent/quickActions";
import SupportPage from "./pages/Support";
import SupportAgentPage from "./pages/SupportAgent";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={SupportAgentPage}></Route>
        <Route path="/s" Component={SupportPage}></Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
