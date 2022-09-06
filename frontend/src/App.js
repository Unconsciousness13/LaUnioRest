import "./App.css";
import "./components/GymnastsList";
import GymnastsList from "./components/GymnastsList";
import TrainersList from "./components/TrainersList";
import Home from "./pages/Home";
import NotFound from "./pages/NotFound";
import Header from "./components/Header";
import { Routes, Route, BrowserRouter } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import "react-toastify/dist/ReactToastify.css";

function App() {
  return (
    <div className="App">
      <Header />
      <ToastContainer position="top-center" />
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/gymnasts" element={<GymnastsList />} />
          <Route path="/trainers" element={<TrainersList />} />
          {/* <Route
          path="/create"
          element={
            user?.uid ? <AddEditGame user={user} /> : <Navigate to="/" />
          }
        /> */}
          {/* <Route
          path="/update/:id"
          element={
            user?.uid ? <AddEditGame user={user} setActive={setActive} /> : <Navigate to="/" />
          }
        /> */}
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
