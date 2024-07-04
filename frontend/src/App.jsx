import { BrowserRouter, Route, Routes } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import ShowOutput from "./pages/ShowOutput";
import Support from "./pages/Support";
import ContactUs from "./pages/ContactUs";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={MainLayout}>
          <Route index Component={ShowOutput} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
