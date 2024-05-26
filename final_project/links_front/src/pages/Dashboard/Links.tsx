import { Button } from '@nextui-org/react';
import useLinkStore from '../../store/linksStore';
import { useEffect } from 'react';

export const Links = () => {
   const { links, fetchLinks, deleteLink, user, postClick } = useLinkStore();
   console.log(user);

   useEffect(() => {
      fetchLinks();
   }, [fetchLinks]);

   const handleDeleteLink = async (id: number) => {
      await deleteLink(id);
   };

   const handleClick = async (linkId: number) => {
      if (!user?.isAdminUser) {
         await postClick(linkId);
      }
   };

   return (
      <div className="m-3 p-3 border rounded-lg">
         <h3 className="text-md font-semibold mb-4">Список ссылок</h3>
         <div className="overflow-x-auto">
            <table className="min-w-full border-collapse border border-gray-200">
               <thead>
                  <tr className="bg-gray-100">
                     <th className="border border-gray-200 p-2 text-left">ID</th>
                     <th className="border border-gray-200 p-2 text-left">Название</th>
                     <th className="border border-gray-200 p-2 text-left">URL</th>
                     <th className="border border-gray-200 p-2 text-left">Описание</th>
                     {user?.isAdminUser && (
                        <th className="border border-gray-200 p-2 text-left">Действия</th>
                     )}
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
                              target="_blank"
                              rel="noopener noreferrer"
                              className="text-blue-500 underline"
                              onClick={() => handleClick(link.id)}
                           >
                              {link.url}
                           </a>
                        </td>
                        <td className="border border-gray-200 p-2">{link.description}</td>
                        {user?.isAdminUser && (
                           <td className="border border-gray-200 p-2">
                              <Button onClick={() => handleDeleteLink(link.id)} color="danger">
                                 Удалить
                              </Button>
                           </td>
                        )}
                     </tr>
                  ))}
               </tbody>
            </table>
         </div>
      </div>
   );
};

export default Links;
