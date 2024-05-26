import { Button } from '@nextui-org/react'
import { useState } from 'react'
import useLinkStore from '../../store/linksStore'

export const Profile = () => {
   const [password, setPassword] = useState('')
   const { user } = useLinkStore()

   return (
      <div className="grid p-5 gap-5">
         <div className="border rounded-lg p-3 grid grid-cols-1 gap-4 max-w-2xl">
            <div>
               <p className="font-semibold text-start text-sm">Имя</p>
               <input
                  type="text"
                  placeholder={user?.username}
                  className="grid border rounded-xl p-2 w-full mt-1"
               />
            </div>
            <div>
               <p className="font-semibold text-start text-sm">Пароль</p>
               <input
                  className="grid border rounded-xl p-2 w-full mt-1"
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="password"
               />
            </div>
            <div className="grid justify-end">
               <Button
                  variant="shadow"
                  className="bg-danger text-white px-7 font-semibold"
               >
                  Сохранить
               </Button>
            </div>
         </div>
      </div>
   )
}
