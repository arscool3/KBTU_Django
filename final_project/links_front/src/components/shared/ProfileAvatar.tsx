import { Avatar } from '@nextui-org/react'
import AvatarImage from './../../assets/home/avatar.png'

export const ProfileAvatar = () => {
   return (
      <div className="relative">
         <Avatar
            src={AvatarImage}
            className="w-14 h-14 text-large border-1 border-gray-300 hover:border-danger-100 cursor-pointer"
         />
         <div className="absolute w-4 h-4 bg-green-500 rounded-full border-2 border-white bottom-0 right-0"></div>
      </div>
   )
}
