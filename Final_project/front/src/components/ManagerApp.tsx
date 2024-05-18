import React, { useState } from "react";
import Button from "@mui/material/Button";
import Dialog from "@mui/material/Dialog";
import DialogActions from "@mui/material/DialogActions";
import DialogContent from "@mui/material/DialogContent";
import DialogContentText from "@mui/material/DialogContentText";
import DialogTitle from "@mui/material/DialogTitle";
import Paper from "@mui/material/Paper";
import Draggable from "react-draggable";
import { Alert, Snackbar, TextField } from "@mui/material";
import MuiAlert from "@mui/material/Alert";
import Header from "../components/Header";
import { useNavigate } from "react-router-dom";
import { PropaneSharp } from "@mui/icons-material";
import axios from "axios";
import ThumbDownIcon from '@mui/icons-material/ThumbDown';

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




const ManagerApp = (props: any) => {
    const [open, setOpen] = React.useState(false);

    const [newError, setNewError] = useState(false);


    const navigate = useNavigate();

    const handleClickOpen = () => {
        setOpen(true);
    };


    const handleClose = () => {
        setOpen(false);

        setNewError(false);
    };

    const handleAccept = (e: any) => {
        e.preventDefault();
        handleClose();
        props.handleSuccess();
        window.location.reload();

    };

    const handleReject = (e: any) => {
        e.preventDefault();
        setOpen(false);
        handleClose();
        props.handleReject();
        setNewError(false);
        window.location.reload();

    };



    const sendData = async (e: any) => {
        try {
            const token = localStorage.getItem("token");

            const config = {
            headers: { Authorization: `Bearer ${token}` }
            };
        
            const response = await axios.patch(
            `http://localhost:8000/manager/app?application_id=${props.id}`,
            {}, 
            config
            );
            
            console.log(props.id);
            handleAccept(e);
        } catch (error: any) {
            console.error("There was an error!", error);
            if(error.message === 'Request failed with status code 503'){
            setNewError(true);
            }
        }
    }

    const rejectData = async (e: any) => {
        try {
            const token = localStorage.getItem("token");

            const config = {
            headers: { Authorization: `Bearer ${token}` }
            };
        
            const response = await axios.patch(
            `http://localhost:8000/manager/no?application_id=${props.id}`,
            {}, 
            config
            );
            
            console.log(props.id);
            handleReject(e);
        } catch (error: any) {
            console.error("There was an error!", error);          
        }
    }


    return (
        <>

            <button onClick={handleClickOpen}>
                Заявка на согласование {props.data.email}
            </button>
            <Dialog
                open={open}
                onClose={handleClose}
                PaperComponent={PaperComponent}
            >
                <div className="userContainerButtonPersonal" >
                    <h1 style={{margin: "15px 0px 20px 0px"}}>Заявка на изменение персональных данных от {props.data.name}</h1>
                    <div>
                        <div>
                            <div style={{display:"flex", flexWrap: "wrap", width: "500px", justifyContent:"center", gap: "10px"}}>
                                <TextField
                                    className="outlined-basic"
                                    label="Имя"
                                    name="FirstName"
                                    variant="outlined"
                                    value={props.data.name}
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Фамилия"
                                    name="Surname"
                                    variant="outlined"
                                    value={props.data.surname}
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Возраст"
                                    name="age"
                                    variant="outlined"
                                    value={props.data.age}
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Дата рождения"
                                    name="birthdate"
                                    variant="outlined"
                                    value={props.data.birthdate}
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="ИИН"
                                    name="IIN"
                                    variant="outlined"
                                    value={props.data.iin}
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    type="email"
                                    name="Email"
                                    label="E-mail"
                                    value={props.data.email}
                                    variant="outlined"
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Номер телефона"
                                    name="PhoneNumber"
                                    variant="outlined"
                                    value={props.data.call}
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="TelegramID"
                                    variant="outlined"
                                    value={props.data.tg_id}
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Университет"
                                    variant="outlined"
                                    value={props.data.university}
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Город"
                                    variant="outlined"
                                    value={props.data.city}
                                    style={{ backgroundColor: "white" }}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Место по прописке"
                                    variant="outlined"
                                    value={props.data.prop_address}
                                    style={{ backgroundColor: "white", width: "300px"}}
                                    disabled
                                />
                                <TextField
                                    className="outlined-basic"
                                    label="Фактическое место проживания"
                                    variant="outlined"
                                    value={props.data.fact_address}
                                    style={{ backgroundColor: "white", width: "300px" }}
                                    disabled
                                />

                            </div>
                            {
                                newError &&
                                <p style={{fontWeight: "bold", color: "red", fontSize: "20px"}}>Клиент с такими данными уже существует!!!</p>
                            }
                            <>
                                <Button onClick={rejectData} className="defaultButton">
                                    Отклонить
                                </Button>
                                <Button onClick={sendData}  className="defaultButton">Одобрить</Button>
                            </>

                            
                        </div>
                    </div>
                </div>
            </Dialog>
        </>
    );
};

export default ManagerApp;
