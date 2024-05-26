import { FC, ReactNode } from 'react';
import { Navigate, Outlet, useLocation } from 'react-router-dom';
import useLinkStore from '../store/linksStore';

interface PrivateRouteProps {
  children?: ReactNode;
}

const PrivateRoute: FC<PrivateRouteProps> = ({ children }) => {
  const { user } = useLinkStore();
  const location = useLocation();

  if (!user) {
    return <Navigate to="/login" state={{ from: location }} />;
  }

  if (!user.isAdminUser && location.pathname !== '/dashboard/links') {
    return <Navigate to="/dashboard/links" />;
  }

  return children ? <>{children}</> : <Outlet />;
};

export default PrivateRoute;
