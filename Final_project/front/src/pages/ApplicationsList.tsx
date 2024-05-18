import React, { useEffect, useState } from 'react'
import Header from '../components/Header'
import ManagerApp from '../components/ManagerApp'
import axios from 'axios';
import { Alert, Snackbar } from '@mui/material';
import { useNavigate } from 'react-router-dom';


const ApplicationsList = (props: any) => {
  const [data, setData] = useState<any[]>([]);
  const [newData, setNewData] = useState<any[]>([]); 
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get('http://localhost:8000/manager/apps');
        console.log(response.data);
        setData(response.data);
      } catch (error) {
        console.error('Error fetching data: ', error);
      }
    };

    fetchData();
  }, []);

  const [success, setSuccess] = React.useState(false);
  const [rejected, setRejected] = React.useState(false);


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


  return (
    <>
      <Header/>
      <div className="applicationsContainer">
      <div className="applications">
        <div className="userApplication">
          {data.map((d, index) => {
            if(d.status === "Under consideration"){ 
              return <div key={index}>
              <ManagerApp handleSuccess={handleSuccess} handleReject={handleReject} data={d.personal_data_changes} id={d.id} status={d.status}/>
              </div>
            }
            
          })
          
          }
        </div>
      </div>
    </div>
      
      

      <Snackbar open={success} autoHideDuration={6000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success" sx={{ width: "100%" }}>
          Заявка была одобрена!
        </Alert>
      </Snackbar>
      <Snackbar open={rejected} autoHideDuration={6000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="error" sx={{ width: "100%" }}>
          Заявка была отклонена!
        </Alert>
      </Snackbar>
    </>
  )
}


export default ApplicationsList