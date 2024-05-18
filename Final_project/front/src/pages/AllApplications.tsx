import React, { useEffect, useState } from 'react'
import Header from '../components/Header'
import ManagerApp from '../components/ManagerApp'
import axios from 'axios';
import { Alert, Snackbar } from '@mui/material';
import { useNavigate } from 'react-router-dom';
import Unchangeable from '../components/Unchangeable';


const AllApplications = (props: any) => {
  const [data, setData] = useState<any[]>([]); // Assuming data is an array of objects
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


  return (
    <>
      <Header/>
      <div className="applicationsContainer">
      <div className="applications">
        <div className="userApplication">
            {data.map((d, index) => {
              return <div key={index}>
              <Unchangeable data={d.personal_data_changes} id={d.id} status={d.status} date={d.updated_at}/>
            </div>
            
          })}
        </div>
      </div>
    </div>
    </>
  )
}


export default AllApplications