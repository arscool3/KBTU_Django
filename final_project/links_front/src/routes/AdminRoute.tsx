// AdminRoute.tsx
import { FC, ReactNode } from 'react';
import { Navigate, useLocation } from 'react-router-dom';
import useLinkStore from '../store/linksStore';

interface AdminRouteProps {
    children: ReactNode;
}

const AdminRoute: FC<AdminRouteProps> = ({ children }) => {
    const { user } = useLinkStore();
    const location = useLocation();

    if (!user?.isAdminUser) {
        // Redirect to /dashboard/links if not an admin
        return <Navigate to="/dashboard/links" state={{ from: location }} />;
    }

    return <>{children}</>;
};

export default AdminRoute;
