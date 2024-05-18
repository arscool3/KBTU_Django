import React, { useState } from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import Paper from "@mui/material/Paper";
import Draggable from "react-draggable";
import { Alert, AlertTitle, Snackbar, TextField } from "@mui/material";
import MuiAlert from "@mui/material/Alert";
import Header from "../components/Header";
import { useNavigate } from "react-router-dom";
import axios from "axios";

function PaperComponent(props: any) {
    return (
        <Draggable
            handle="#draggable-dialog-title"
            cancel={'[class*="MuiDialogContent-root"]'}
        >
            <Paper {...props} />
        </Draggable>
    );
}


const ButtonPersonal = (props: any) => {
    const item = localStorage.getItem("user");
    const data: any = item ? JSON.parse(item) : null;
    const [open, setOpen] = React.useState(false);
    const [rejected, setRejected] = React.useState(false);
    const [firstname, setFirstname] = useState(data.name);
    const [surname, setSurname] = useState(data.surname);
    const [email, setEmail] = useState(data.email);
    const [phoneNumber, setPhoneNumber] = useState(data.call);
    const [IIN, setIIN] = useState(data.iin);
    const [tg_id, setTg_id] = useState(data.tg_id);
    const [university, setUniversity] = useState(data.university);
    const [city, setCity] = useState(data.city);
    const [age, setAge] = useState(data.age);
    const [birthdate, setBirthdate] = useState(data.birthdate);
    const [fact_address, setFact_address] = useState(data.fact_address);
    const [prop_address, setProp_address] = useState(data.fact_address);
    const [is_disabled, setIs_disabled] = useState(false);
    const const_email = email;
    


    const navigate = useNavigate();

    const handleClickOpen = () => {
        setOpen(true);
    };

    const handleAccept = async (e: any) => {
        e.preventDefault();
        setOpen(false);
        setIs_disabled(false);

        const item = {
            name: firstname,
            surname: surname,
            birthdate:birthdate,
            iin: IIN,
            email: email,
            call: phoneNumber,
            city: city,
            tg_id: tg_id,
            age: age,
            fact_address: fact_address,
            prop_address: prop_address,
            university: university
        };


        try {
            const token = localStorage.getItem("token");
            const response = await axios.post('http://localhost:8000/user', item, {
                headers: {
                  'Authorization': `Bearer ${token}`
                }
            });
            console.log("response.data");
            props.handleSuccess();
        } catch (error: any) {
            console.error("There was an error!", error);
            if(error.message === "Request failed with status code 403"){
                props.handleAlert();
            }
        }

        axios.get(`http://localhost:8000/user/${const_email}`, 
        {
          headers: {
            "content-type": "application/json" 
          },
        })
        .then((res: any) => {

            localStorage.setItem('user', JSON.stringify(res.data));
        })
            .catch((error: any) => {
            console.log('axios: ' + error);
    
        });

    };

    const handleReject = () => {
        setOpen(false);
        setRejected(true);

    };

    const handleCheck = () => {
        setIs_disabled(true);
    }

    const handleClose = () => {
        setOpen(false);
        setRejected(false);
    };


    return (
        <>

            <button onClick={handleClickOpen}>
                Заявка на изменение персональных данных
            </button>
            <Dialog
                open={open}
                onClose={handleClose}
                PaperComponent={PaperComponent}
            >
                <div className="userContainerButtonPersonal" >
                    <h1 style={{margin: "15px 0px 20px 0px"}}>Заявка на изменение персональных данных</h1>
                    <div>
                        <div>
                            <div style={{display:"flex", flexWrap: "wrap", width: "500px", justifyContent:"center", gap: "10px"}}>
                                <TextField
                                    className="outlined-basic"
                                    label="Имя"
                                    name="FirstName"
                                    variant="outlined"
                                    value={firstname}
                                    onChange={(e: any) => setFirstname(e.target.value)}
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Фамилия"
                                    name="Surname"
                                    variant="outlined"
                                    value={surname}
                                    onChange={(e: any) => setSurname(e.target.value)}
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Возраст"
                                    name="age"
                                    variant="outlined"
                                    value={age}
                                    onChange={(e: any) => setAge(e.target.value)}
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Дата рождения"
                                    name="birthdate"
                                    variant="outlined"
                                    value={birthdate}
                                    onChange={(e: any) => setBirthdate(e.target.value)}
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="ИИН"
                                    name="IIN"
                                    variant="outlined"
                                    value={IIN}
                                    onChange={(e: any) => setIIN(e.target.value)}
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    type="email"
                                    name="Email"
                                    label="E-mail"
                                    value={email}
                                    onChange={(e: any) => setEmail(e.target.value)}
                                    variant="outlined"
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />

                                <TextField
                                    className="outlined-basic"
                                    label="Номер телефона"
                                    name="PhoneNumber"
                                    variant="outlined"
                                    value={phoneNumber}
                                    onChange={(e: any) => setPhoneNumber(e.target.value)}
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="TelegramID"
                                    variant="outlined"
                                    value={tg_id}
                                    onChange={(e: any) => setTg_id(e.target.value)}
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Университет"
                                    variant="outlined"
                                    value={university}
                                    onChange={(e: any) => setUniversity(e.target.value)}
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Город"
                                    variant="outlined"
                                    value={city}
                                    onChange={(e: any) => setCity(e.target.value)}
                                    style={{ backgroundColor: "white" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Место по прописке"
                                    variant="outlined"
                                    value={prop_address}
                                    onChange={(e: any) => setProp_address(e.target.value)}
                                    style={{ backgroundColor: "white", width: "300px" }}
                                    disabled={is_disabled}
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Фактическое место проживания"
                                    variant="outlined"
                                    value={fact_address}
                                    onChange={(e: any) => setFact_address(e.target.value)}
                                    style={{ backgroundColor: "white", width: "300px" }}
                                    disabled={is_disabled}
                                />

                            </div>
                            
                            {
                                is_disabled &&
                                <>
                                    <Button autoFocus onClick={() => {setIs_disabled(false)}} style={{ backgroundColor: "green", margin: "30px", padding:"10px", color:"white"  }}>
                                        Назад
                                    </Button>
                                    <Button onClick={handleAccept}  style={{ backgroundColor: "green", margin: "30px", padding:"10px", color:"white" }}>Отправить</Button>
                                </>
                                
                            }
                            {

                                !is_disabled &&
                                <>                                
                                <Button autoFocus onClick={handleReject} style={{ backgroundColor: "green", margin: "30px", padding:"10px", color:"white"  }}>
                                    Отменить
                                </Button>
                                <Button onClick={handleCheck}  style={{ backgroundColor: "green", margin: "30px", padding:"10px", color:"white" }}>Проверить и отправить</Button>

                                </>
                            }
                            
                            
                        </div>
                    </div>
                </div>
            </Dialog>
        </>
    );
};

export default ButtonPersonal;
