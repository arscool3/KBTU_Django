import React, { useEffect, useState } from "react";
import Autorize from "./Autorize";
import UserButton from "./UserButton";
import { Await, useNavigate } from "react-router-dom";
import axios from "axios";


const Header = (props: any) => {

  const [username, setUsername] = useState<null | string>(localStorage.getItem("username"));

  const item = localStorage.getItem("user");
  const data: any = item ? JSON.parse(item) : null;


  
  const deleteUser = () => {
    setUsername(null);
    localStorage.clear();
  }

  const navigate = useNavigate();
  return (
    <>
      <div className="header">
        <div className="headerButtons">
          <button>ҚАЗ</button>
          <button>РУС</button>
          <button>ENG</button>
        </div>
        {!username &&
          <Autorize/>
        }
        {username &&
          <UserButton user={username} deleteUser={deleteUser}/>
        }
      </div>
      
      <div className="categories">
        {data && data.roles === "ROLE_PORTAL_PHIS" &&
          <>
          <button  onClick={() => {
            navigate("/user/applications")
          }} className={window.location.pathname === "/user/applications" ? "categoryButton active" : "categoryButton"}>Заявки</button>
          <button  onClick={() => {
            navigate("/user/myApplications")
          }} className={window.location.pathname === "/user/myApplications" ? "categoryButton active" : "categoryButton"}>Мои заявки</button>
          </>
          
        }
        {data &&data.roles === "ROLE_PORTAL_MNG" &&
          <>
            <button onClick={() => {
              navigate("/user/applicationsList")
            }} className={window.location.pathname === "/user/applicationsList" ? "categoryButton active" : "categoryButton"}>Список заявок</button>
              <button onClick={() => {
              navigate("/user/allApplications")
            }} className={window.location.pathname === "/user/allApplications" ? "categoryButton active" : "categoryButton"}>Все заявки</button>
          </>
          
        }
        <button onClick={() => {
          navigate("/user/profile")
        }} className={window.location.pathname === "/user/profile" ? "categoryButton active" : "categoryButton"}>Профиль</button>

  
      </div>
    </>
  );
};

export default Header;
