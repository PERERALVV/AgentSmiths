import { BrowserRouter, Route, Routes } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import Home from "./pages/Home";
import ShowOutput from "./pages/ShowOutput";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={MainLayout}>
          <Route index Component={ShowOutput} />
          <Route index Component={Home} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
