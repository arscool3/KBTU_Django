import { Outlet } from 'react-router-dom'

export const RootPage = () => {
   return (
      <div>
         <section>
            {' '}
            <Outlet />{' '}
         </section>
      </div>
   )
}
