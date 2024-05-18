import axios from 'axios';
import { Button, TextField } from "@mui/material";
import React, { ChangeEvent, useState } from "react";
import { useNavigate } from 'react-router';

const Registration = () => {

    const [firstname, setFirstName] = useState("");
    const [surname, setSurname] = useState("");
    const [password, setPassword] = useState("");
    const [email, setEmail] = useState("");
    const [phoneNumber, setPhoneNumber] = useState("");
    const [IIN, setIIN] = useState("");
    const [tg_id, setTg_id] = useState("");
    const navigate = useNavigate();
    

    const handleSubmit = async (e: any) => {
        const item = {
            name: firstname,
            surname: surname,
            password: password,
            iin: IIN,
            email: email,
            call: phoneNumber,
            tg_id: tg_id
        };


        try {
            const response = await axios.post('http://localhost:8000/user/register', item);
            console.log("response.data");
        } catch (error) {
            console.error("There was an error!", error);
        }

        
        navigate("/login")
    };

    return (
        <div className="registration">
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
          <a href="/login">Войти</a>
        </div>
      </div>

      <div className="loginContainer">
        <p className="loginTitle">Регистрация на портал</p>
          <TextField
            className="outlined-basic"
            label="Имя"
            name="FirstName"
            variant="outlined"
            value={firstname}
            onChange={(e:any) => setFirstName(e.target.value)}
            style={{ backgroundColor: "white" }}
          />
          <TextField
            className="outlined-basic"
            label="Фамилия"
            name="Surname"
            variant="outlined"
            value={surname}
            onChange={(e:any) => setSurname(e.target.value)}
            style={{ backgroundColor: "white" }}
          />
          <TextField
            className="outlined-basic"
            label="ИИН"
            name="IIN"
            variant="outlined"
            value={IIN}
            onChange={(e:any) => setIIN(e.target.value)}
            style={{ backgroundColor: "white" }}
          />
          <TextField
            className="outlined-basic"
            type="email"
            name="Email"
            label="E-mail"
            value={email}
            onChange={(e:any) => setEmail(e.target.value)}
            variant="outlined"
            style={{ backgroundColor: "white" }}
          />
          <TextField
            className="outlined-basic"
            type="password"
            name="Password"
            label="Пароль"
            value={password}
            onChange={(e:any) => setPassword(e.target.value)}
            variant="outlined"
            style={{ backgroundColor: "white" }}
          />
          
          <TextField
            className="outlined-basic"
            label="Номер телефона"
            name="PhoneNumber"
            variant="outlined"
            value={phoneNumber}
            onChange={(e:any) => setPhoneNumber(e.target.value)}
            style={{ backgroundColor: "white" }}
          />
          <TextField
            className="outlined-basic"
            label="TelegramID"
            variant="outlined"
            value={tg_id}
            onChange={(e:any) => setTg_id(e.target.value)}
            style={{ backgroundColor: "white" }}
          />
          <Button variant="contained" style={{ backgroundColor: "green" }} onClick={handleSubmit}>
            Регистрация
          </Button>
      </div>
    </div>
    );
}

export default Registration;