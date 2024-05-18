import React, { useState } from "react";
import "./app.css";
import { BrowserRouter, Navigate, Route, Routes, useNavigate } from "react-router-dom";
import Home from "./pages/Home";
import Login from "./pages/Login";
import Registration from "./pages/Registration";
import Profile from "./pages/Profile";
import Applications from "./pages/Applications";
import ApplicationsList from "./pages/ApplicationsList";
import AllApplications from "./pages/AllApplications";
import MyApplications from "./pages/MyApplications";

type UserPropsType = {
  userId: string;
  firstname: string;
  surname: string;
  password: string;
  IIN:string;
  email: string;
  phonenumber: string;
};

function App() {
  // const [user, setUser] = useState<UserPropsType | null>({
  //   userId: "12345",
  //   firstname: "Amina",
  //   surname: "Matova",
  //   password: "djvadfvnkajsfv",
  //   IIN: "2476284752485",
  //   email: "adcadcadcadc",
  //   phonenumber: "3412374123"
  // });
  

  return (
    <BrowserRouter>
      <Routes>
      <Route path="/" element={<Navigate to="/login"/>} />
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/registration" element={<Registration/>} />
        <Route path="/user/profile" element={<Profile/>} />
        <Route path="/user/applications" element={<Applications />} />
        <Route path="/user/applicationsList" element={<ApplicationsList />} />
        <Route path="/user/allApplications" element={<AllApplications />} />
        <Route path="/user/myApplications" element={<MyApplications />} />
      </Routes>
    </BrowserRouter>
  );    
}

export default App;
