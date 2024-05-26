import { Divider } from '@nextui-org/react'

export const DashboardFooter = () => {
   return (
      <div className="pt-[2em]">
         <Divider />
         <div className="flex justify-between px-5 py-3">
            <a
               href="https://irocket.kz/policy"
               className="text-tiny text-gray-500 hover:text-danger"
            >
               Пользовательское соглашение
            </a>
            <p className="text-tiny text-gray-500">
               2023 iRocket © Все права защищены
            </p>
         </div>
      </div>
   )
}
