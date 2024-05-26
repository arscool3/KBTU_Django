import { useEffect } from 'react'
import useLinkStore from '../../store/linksStore'

export const Analytics = () => {
   const { links, fetchLinks, fetchClicks, clicks } = useLinkStore()

   useEffect(() => {
      fetchLinks()
      fetchClicks()
   }, [fetchLinks, fetchClicks])

   const getClickCount = (linkId: number) => {
      return clicks.filter((click) => click.link === linkId).length
   }

   return (
      <div className="grid p-5 gap-5">
         <div className="grid border rounded-lg p-2">
            <div className="overflow-x-auto">
               <table className="min-w-full border-collapse border border-gray-200">
                  <thead>
                     <tr className="bg-gray-100">
                        <th className="border border-gray-200 p-2 text-left">
                           ID
                        </th>
                        <th className="border border-gray-200 p-2 text-left">
                           URL
                        </th>
                        <th className="border border-gray-200 p-2 text-left">
                           Название
                        </th>
                        <th className="border border-gray-200 p-2 text-left">
                           Описание
                        </th>
                        <th className="border border-gray-200 p-2 text-left">
                           Количество переходов
                        </th>
                     </tr>
                  </thead>
                  <tbody>
                     {links.map((link) => (
                        <tr key={link.id}>
                           <td className="border border-gray-200 p-2">
                              {link.id}
                           </td>
                           <td className="border border-gray-200 p-2">
                              <a
                                 href={link.url}
                                 target="_blank"
                                 rel="noopener noreferrer"
                                 className="text-blue-500 underline"
                                 >
                                 {link.url}
                              </a>
                           </td>
                           <td className="border border-gray-200 p-2">
                              {link.title}
                           </td>
                           <td className="border border-gray-200 p-2">
                              {link.description}
                           </td>
                           <td className="border border-gray-200 p-2">
                              {getClickCount(link.id)}
                           </td>
                        </tr>
                     ))}
                  </tbody>
               </table>
            </div>
            {links.length === 0 && (
               <p className="grid justify-center items-center text-danger">
                  товары не найдены !
               </p>
            )}
         </div>
      </div>
   )
}

export default Analytics
