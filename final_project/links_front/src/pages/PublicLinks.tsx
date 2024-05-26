import { useEffect } from 'react'
import { Button } from '@nextui-org/react'
import { useNavigate } from 'react-router-dom'
import useLinkStore from '../store/linksStore'
import { Logo } from '../components/shared/Logo'

export const PublicLinks = () => {
   const { links, fetchLinks, postClick } = useLinkStore()
   const navigate = useNavigate()

   useEffect(() => {
      fetchLinks()
   }, [fetchLinks])

   const handleLoginClick = () => {
      navigate('/login')
   }

   return (
      <div className="m-3 p-3 border rounded-lg">
         <div className="flex justify-between items-center">
            <Logo />
            <Button onClick={handleLoginClick} color="danger">
               Вход
            </Button>
         </div>
         <div className="flex justify-between items-center mb-4">
            <h3 className="text-md font-semibold">Список ссылок</h3>
         </div>
         <div className="overflow-x-auto">
            <table className="min-w-full border-collapse border border-gray-200">
               <thead>
                  <tr className="bg-gray-100">
                     <th className="border border-gray-200 p-2 text-left">ID</th>
                     <th className="border border-gray-200 p-2 text-left">Название</th>
                     <th className="border border-gray-200 p-2 text-left">URL</th>
                     <th className="border border-gray-200 p-2 text-left">Описание</th>
                  </tr>
               </thead>
               <tbody>
                  {links.map((link) => (
                     <tr key={link.id}>
                        <td className="border border-gray-200 p-2">{link.id}</td>
                        <td className="border border-gray-200 p-2">{link.title}</td>
                        <td className="border border-gray-200 p-2">
                           <a
                              href={link.url}
                              onClick={() => {
                                 postClick(link.id)
                              }}
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-blue-500 underline"
                           >
                              {link.url}
                           </a>
                        </td>
                        <td className="border border-gray-200 p-2">{link.description}</td>
                     </tr>
                  ))}
               </tbody>
            </table>
         </div>
      </div>
   )
}

export default PublicLinks
