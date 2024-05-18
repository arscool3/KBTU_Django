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


const ButtonBIN = () => {
  const [open, setOpen] = React.useState(false);

  const item = localStorage.getItem("user");
  const data: any = item ? JSON.parse(item) : null;

  const [bin, setBin] = useState("");
  const [company, setCompany] = useState("");
  const [isAllowed, setIsAllowed] = useState(false);
  const [error, setError] = useState(false);

  const handleClickOpen = () => {
    setOpen(true);
  };

  const handleClose = () => {
    setOpen(false);
    setBin("");
    setCompany("");
    setIsAllowed(false);

  };

  const sendBIN = async (e: any) => {
    try {
        const config = {
            headers: { "accept": "application/json" }
        };

        const response = await axios.get(`http://172.20.10.5:1214/process_bin?bin=${bin}`, config);


        console.log(response.data);
        setIsAllowed(true);
        setCompany(response.data.name);
        
    } catch (error: any) {
        console.error("There was an error!", error);
        
        if (error.response && error.response.status === 404) {
            setError(true);
        } 
    }
  };

  document.addEventListener("click", () => {
    setError(false);
  });

  const sendRequest = async (e: any) => {
    try {
        const config = {
            headers: { "accept": "application/json" }
        };

        const info = {
          email: data.email,
          tg_id: data.tg_id
        }

        const dat = `http://172.20.10.5:1214/get_data?bin=${bin}&user=${encodeURIComponent(JSON.stringify(info))}`
        const response = await axios.post(dat, config);
        console.log(response.data);
        handleClose();
    } catch (error: any) {
        console.error("There was an error!", error);

        // Check specific error conditions
        if (error.response && error.response.status === 404) {
            setError(true);
        } else {
            // Handle other types of errors
        }
    }
  };


  return (
    <>
            <button onClick={handleClickOpen}>
               Заявка на справку по Юр.Лицу
            </button>
            <Dialog
              open={open}
              onClose={handleClose}
              PaperComponent={PaperComponent}
              aria-labelledby="draggable-dialog-title"

            >
              <DialogTitle
                style={{ cursor: "move", fontSize: "30px", fontWeight: "bold", padding: "30px 60px 50px 60px" }}
                id="draggable-dialog-title"
              >
                Заявка на справку по Юр.Лицу
              </DialogTitle>
              <DialogContent>
                <DialogContentText style={{ display:"flex", flexDirection: "column", gap: "20px", alignItems: "center"}}>
                <TextField
                  className="outlined-basic"
                  label="BIN"
                  name="BIN"
                  variant="outlined"
                  value={bin}
                  onChange={(e:any) => {setBin(e.target.value);setError(false);}}
                  style={{ backgroundColor: "white", width: "450px", margin: "20px 0px" }}
                />
                {isAllowed &&
                  <TextField
                    className="outlined-basic"
                    label="Company"
                    name="company"
                    variant="outlined"
                    value={company}
                    onChange={(e:any) => {setCompany(e.target.value);setError(false);}}
                    style={{ backgroundColor: "white", width: "450px" }}
    
                  />
                }
                
                {error && 
                  <p style={{color: "red", fontSize: "25px"}}>Данный BIN не найден!!!</p>
                }
                </DialogContentText>
                
              </DialogContent>
              <DialogActions>
              <Button onClick={sendBIN} style={{ backgroundColor: "green", margin: "30px", padding:"10px", color:"white"  }}>
                  Проверить
              </Button>
              <Button onClick={sendRequest} disabled={!isAllowed} style={isAllowed ? { backgroundColor: "green", margin: "30px", padding:"10px", color:"white", cursor: "pointer"} : { backgroundColor: "rgb(226, 255, 226)", margin: "30px", padding:"10px", color:"white", cursor: "default" }}>Одобрить</Button>
              </DialogActions>
            </Dialog>
    </>
  );
};

export default ButtonBIN;
