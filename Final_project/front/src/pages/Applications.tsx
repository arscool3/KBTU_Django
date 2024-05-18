import React, { useState } from "react";
import ManagerApp from "../components/ManagerApp";
import UserApp from "../components/UserApp";
import Header from "../components/Header";
import { Alert, AlertTitle, Snackbar, Stack } from "@mui/material";


const Applications = () => {

  const [success, setSuccess] = useState(false);
  const [rejected, setRejected] = useState(false);
  const [isAlert, setIsAlert] = useState(false);


  const handleClose = () => {
    setSuccess(false);
    setRejected(false);
  };

  const handleSuccess = () => {
    setSuccess(true);
  }

  const handleReject = () => {
    setRejected(true);
  }

  const handleAlert = () => {
    setIsAlert(true);
  }

  document.addEventListener("click", () => {
    setIsAlert(false);
  })



  return (
    <>
      <Header />
      {isAlert &&
        <Stack sx={{ width: '100%' }} spacing={2}>
          <Alert  severity="error">
              <AlertTitle>Error</AlertTitle>
              Запрос от этого Пользователя уже существует — <strong>Ждите ответа Менеджера!</strong>
          </Alert>
        
        </Stack>
      } 
      <UserApp handleSuccess={handleSuccess} handleAlert={handleAlert}/>

      <Snackbar open={success} autoHideDuration={6000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success" sx={{ width: "100%" }}>
          Заявка была принята!
        </Alert>
      </Snackbar>
      <Snackbar open={rejected} autoHideDuration={6000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="error" sx={{ width: "100%" }}>
          Заявка была отклонена!
        </Alert>
      </Snackbar>
    </>
  );
};

export default Applications;
