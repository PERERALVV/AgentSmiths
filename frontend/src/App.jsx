import { BrowserRouter, Route, Routes } from "react-router-dom";
import MainLayout from "./layouts/MainLayout";
import ShowOutput from "./pages/ShowOutput";
import Support from "./pages/Support";

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" Component={MainLayout}>
          {/* <Route index Component={Support} /> */}
          <Route index Component={ShowOutput} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
};

export default App;
