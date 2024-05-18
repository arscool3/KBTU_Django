import React from "react";
import { styled, alpha } from '@mui/material/styles';
import Button from '@mui/material/Button';
import Menu, { MenuProps } from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import EditIcon from '@mui/icons-material/Edit';
import Divider from '@mui/material/Divider';
import ArchiveIcon from '@mui/icons-material/Archive';
import FileCopyIcon from '@mui/icons-material/FileCopy';
import MoreHorizIcon from '@mui/icons-material/MoreHoriz';
import KeyboardArrowDownIcon from '@mui/icons-material/KeyboardArrowDown';
import { useNavigate } from "react-router-dom";

const StyledMenu = styled((props: MenuProps) => (
    <Menu
      elevation={0}
      anchorOrigin={{
        vertical: 'bottom',
        horizontal: 'right',
      }}
      transformOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      {...props}
    />
  ))(({ theme }) => ({
    '& .MuiPaper-root': {
      borderRadius: 6,
      marginTop: theme.spacing(1),
      minWidth: 160,
      color:
        theme.palette.mode === 'light' ? 'rgb(55, 65, 81)' : theme.palette.grey[300],
      boxShadow:
        'rgb(255, 255, 255) 0px 0px 0px 0px, rgba(0, 0, 0, 0.05) 0px 0px 0px 1px, rgba(0, 0, 0, 0.1) 0px 10px 15px -3px, rgba(0, 0, 0, 0.05) 0px 4px 6px -2px',
      '& .MuiMenu-list': {
        padding: '4px 0',
      },
      '& .MuiMenuItem-root': {
        '& .MuiSvgIcon-root': {
          fontSize: 18,
          color: theme.palette.text.secondary,
          marginRight: theme.spacing(1.5),
        },
        '&:active': {
          backgroundColor: alpha(
            theme.palette.primary.main,
            theme.palette.action.selectedOpacity,
          ),
        },
      },
    },
  }));

const UserButton = (props: any) => {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const open = Boolean(anchorEl);
  const handleClick = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };
  const handleClose = () => {
    setAnchorEl(null);
    
  };
    const navigate = useNavigate();
    const Logout = () => {
      localStorage.removeItem("token");
      props.deleteUser();
      navigate("/login");
    }

    const item = localStorage.getItem("user");
    const data: any = item ? JSON.parse(item) : null;

    const renderMenuItems = () => {
      let menuItems = [];
  
      if (data.roles === "ROLE_PORTAL_MNG") {
        menuItems.push(
          <MenuItem key="applicationsList" onClick={() => {
            handleClose();
            navigate("/user/applicationsList");
          }}>
            Список заявок
          </MenuItem>,
          <MenuItem key="allApplications" onClick={() => {
            handleClose();
            navigate("/user/allApplications");
          }}>
            Все заявки
          </MenuItem>
        );
      }
  
      if (data.roles === "ROLE_PORTAL_PHIS") {
        menuItems.push(
          <MenuItem key="applications" onClick={() => {
            handleClose();
            navigate("/user/applications");
          }}>
            Заявки
          </MenuItem>,
          <MenuItem key="myApplications" onClick={() => {
            handleClose();
            navigate("/user/myApplications");
          }}>
            Мои заявки
          </MenuItem>
        );
      }
  

      menuItems.push(
        <MenuItem key="profile" onClick={() => {
          handleClose();
          navigate("/user/profile");
        }}>
          Профиль
        </MenuItem>,
        <MenuItem key="logout" onClick={Logout}>
          Выйти
        </MenuItem>
      );
  
      return menuItems;
    };

  return (
    <div className="userButton">
      <Button
        id="demo-customized-button"
        aria-controls={open ? 'demo-customized-menu' : undefined}
        aria-haspopup="true"
        aria-expanded={open ? 'true' : undefined}
        variant="contained"
        disableElevation
        onClick={handleClick}
        endIcon={<KeyboardArrowDownIcon />}
        style={{ backgroundColor: "green"}}
      >
        {props.user}
      </Button>
      <StyledMenu
        id="demo-customized-menu"
        MenuListProps={{
          'aria-labelledby': 'demo-customized-button',
        }}
        anchorEl={anchorEl}
        open={open}
        onClose={handleClose}
      >
        {renderMenuItems()}
      </StyledMenu>
    </div>
  );
};

export default UserButton;
