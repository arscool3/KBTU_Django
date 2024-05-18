import { Button, TextField } from "@mui/material";
import axios from "axios";
import React, { ChangeEvent, useState } from "react";
import { useNavigate } from "react-router";

const Login = () => {


  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const [error, setError] = useState(false);


  const handleSubmit = async (e: any) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append('username', login);
    formData.append('password', password);

    try {
      const response = await axios.post('http://localhost:8000/login/token', formData, {
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      });
      console.log(response);
      const token = response.data.access_token;
      localStorage.setItem("token", token); 

      const payload = JSON.parse(atob(token.split('.')[1]));
      localStorage.setItem("username", payload.sub);

      axios.get(
       `http://localhost:8000/user/${payload.sub}`, 
       {
         headers: {
           'Content-Type': 'application/x-www-form-urlencoded'
         },
       }
     )
     .then((res: any) => {
       localStorage.setItem('user', JSON.stringify(res.data));
       navigate("/home");
     })
     .catch((error: any) => {
       console.log('axios: ' + error);

     });


      

    } catch (error) {
      console.error("There was an error!", error);
      setError(true);
    }
  }

  const handleLoginChange = (e: ChangeEvent<HTMLInputElement>) => {
    setLogin(e.target.value);
    setError(false);
  };

  const handlePasswordChange = (e: ChangeEvent<HTMLInputElement>) => {
    setPassword(e.target.value);
    setError(false);
  };

  return (
    <div className="login">
      <div className="loginHeader">
        <div className="loginLogo">
          <img
            src="https://idp.egov.kz/idp/images/logoegov-e7e0829bcb587b1ad9b6e2cf64023c9f.png"
            alt=""
            style={{ border: "none", borderRight: "1px solid lightGray" }}
          />
          <p>1414</p>
        </div>
        <div className="loginRegister">
          <a href="/registration">Зарегистрироваться</a>
        </div>
      </div>

      <div className="loginContainer">
        <p className="loginTitle">Вход на портал</p>
        <form onSubmit={handleSubmit}>
          <TextField
            id="outlined-basic"
            label="Логин"
            variant="outlined"
            type="email"
            onChange={handleLoginChange}
            value={login}
            style={{backgroundColor: "white"}}
          />
          <TextField
            id="outlined-basic"
            label="Пароль"
            variant="outlined"
            type="password"
            style={{backgroundColor: "white"}}
            onChange={handlePasswordChange}
            value={password}
          />
          {error &&
            <p style={{color: "red", fontSize: "20px", padding: "10px"}}>Wrong login or password!!!</p>
          }
          <Button variant="contained" style={{backgroundColor: "green"}} onClick={handleSubmit}>
            Login
          </Button>
        </form>
      </div>
    </div>
  );
};

export default Login;
