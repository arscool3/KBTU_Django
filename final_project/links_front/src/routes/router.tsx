import { createBrowserRouter, RouteObject } from 'react-router-dom';
import { RootPage } from '../pages/Root/RootPage';
import { Error } from '../pages/Root/Error';
import Dashboard from '../pages/Dashboard/Dashboard';
import { LoginPage } from '../pages/LoginPage';
import { RegisterPage } from '../pages/RegisterPage';
import { Analytics } from '../pages/Dashboard/Analytics';
import DashboardContent from '../pages/Dashboard/DashboardContent';
import { Profile } from '../pages/Dashboard/Profile';
import PrivateRoute from './PrivateRoute';
import AuthRedirect from './AuthRedirect';
import { Links } from '../pages/Dashboard/Links';
import PublicLinks from '../pages/PublicLinks';
import AdminRoute from './AdminRoute';

export const router = createBrowserRouter([
  {
    path: '/',
    element: (
      <AuthRedirect>
        <RootPage />
      </AuthRedirect>
    ),
    errorElement: <Error />,
    children: [
      {
        path: 'links',
        element: <PublicLinks />,
        errorElement: <Error />
      },
    ],
  },
  {
    path: '/login',
    element: (
      <AuthRedirect>
        <LoginPage />
      </AuthRedirect>
    ),
    errorElement: <Error />,
  },
  {
    path: '/register',
    element: (
      <AuthRedirect>
        <RegisterPage />
      </AuthRedirect>
    ),
    errorElement: <Error />,
  },
  {
    path: '/dashboard',
    element: <PrivateRoute />, // Use PrivateRoute for /dashboard and its children
    errorElement: <Error />,
    children: [
      {
        path: '',
        element: <Dashboard />,
        errorElement: <Error />,
        children: [
          {
            path: '',
            element: <DashboardContent />,
            errorElement: <Error />,
          },
          {
            path: 'analytics',
            element: (
              <AdminRoute>
                <Analytics />
              </AdminRoute>
            ),
            errorElement: <Error />,
          },
          {
            path: 'profile',
            element: (
              <AdminRoute>
                <Profile />
              </AdminRoute>
            ),
            errorElement: <Error />,
          },
          {
            path: 'links',
            element: <Links />,
            errorElement: <Error />
          }
        ],
      },
    ],
  },
] as RouteObject[]);
