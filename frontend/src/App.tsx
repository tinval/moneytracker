import { Routes, Route, Navigate } from "react-router-dom";
import Layout from "./components/Layout";
import Main from "./pages/Main";
import Accounts from "./pages/Accounts";
import Transactions from "./pages/Transactions";
import User from "./pages/User";
import NotFound from "./pages/NotFound";

export default function App() {
  return (
    <Routes>
      <Route element={<Layout />}>
        <Route index element={<Main />} />
        <Route path="/accounts" element={<Accounts />} />
        <Route path="/transactions" element={<Transactions />} />
        <Route path="/user" element={<User />} />
        <Route path="/404" element={<NotFound />} />
        <Route path="*" element={<Navigate to="/404" replace />} />
      </Route>
    </Routes>
  );
}
