import { FC, ReactNode } from 'react';
import { Navigate } from 'react-router-dom';
import useLinkStore from '../store/linksStore';

interface AuthRedirectProps {
    children: ReactNode;
}

const AuthRedirect: FC<AuthRedirectProps> = ({ children }) => {
    const refreshToken = localStorage.getItem('refresh_token');
    const { user } = useLinkStore();

    if (refreshToken) {
        if (user?.isAdminUser) {
            return <Navigate to="/dashboard" />;
        }
    }

    return <>{children}</>;
};

export default AuthRedirect;
