import React from "react";
import PersonOutlineIcon from '@mui/icons-material/PersonOutline';

const Autorize = () => {
  return (
    <div className="headerLogin">
      <p>
        <PersonOutlineIcon style={{ color: "green" }} />
      </p>
      <p>
        <a href="/login">Войти</a> или <a href="">Зарегистрироваться</a>
      </p>
    </div>
  );
};

export default Autorize;
