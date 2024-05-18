import React, { useEffect } from "react";
import Header from "../components/Header";


const Profile = (props: any) => {


    const item = localStorage.getItem("user");
    const data: any = item ? JSON.parse(item) : null;
    console.log(data);
  

  return (
    <>
      <Header />
      <div className="profileContainer">
        <div className="profile">
          <div className="profile left">
            <img src="https://my.egov.kz/images/043d2c34.female.png" alt="" style={{width: "150px", borderRadius: "50%"}}/>
            <p>{data.name}</p>
          </div>
          <div className="profile right">
            <p>{data.name}</p>
            <div className="allInfo">
              <div style={{display:"flex", gap: "10px", flexDirection: "column"}}>
                <div>ИИН: {data.iin}</div>
                <div>Возраст: {data.age}</div>
                <div>Дата рождения: {data.birthdate}</div>
                <div>Город: {data.city}</div>
                <div>Университет: {data.university}</div>
              </div>

              <div style={{display:"flex", gap: "10px", flexDirection: "column"}}>
                <div>Фактическое место проживания: {data.fact_address}</div>
                <div>Проживание по прописке: {data.prop_address}</div>
                <div>E-mail: {data.email} </div>
                <div>Телефон: {data.call} </div>
                <div>Telegram ID: {data.tg_id} </div>

              </div>
            </div>
          </div>
        </div>
      </div>
    </>
  );
};

export default Profile;
