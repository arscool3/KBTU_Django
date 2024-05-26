import DashboardHeader from '../../components/shared/DashboardHeader'
import { DashboardFooter } from '../../components/shared/DashboardFooter'
import { Outlet } from 'react-router-dom'
import useLinkStore from '../../store/linksStore'
import { useEffect } from 'react'

const Dashboard = () => {
   const { refreshToken } = useLinkStore()

   useEffect(() => {
      refreshToken()
   }, [refreshToken])

   document.title = 'Панель управления'

   return (
      <div className="flex flex-col min-h-screen">
         <DashboardHeader />
         <div className="flex-grow">
            <Outlet />
         </div>
         <DashboardFooter />
      </div>
   )
}

export default Dashboard
