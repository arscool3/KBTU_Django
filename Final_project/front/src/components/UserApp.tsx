import React from "react";
import ButtonPersonal from "./ButtonPersonal";
import ButtonBIN from "./ButtonBIN";

const UserApp = (props: any) => {
  return (
    <div className="applicationsContainer">
      <div className="applications">
        <div className="userApplication">
          <ButtonPersonal handleSuccess={props.handleSuccess} handleAlert={props.handleAlert}/>
          <ButtonBIN />
        </div>
      </div>
    </div>
  );
};

export default UserApp;