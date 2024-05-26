import { Textarea, Button, Input, Select, SelectItem } from '@nextui-org/react'
import { useState, useEffect } from 'react'
import useStore from '../../store/linksStore'
import { LinkInput } from '../../core/interfaces'

interface NewLinkState {
   id?: number
   url?: string
   title?: string
   description?: string
   category?: number
   tags?: number[]
}

const formatUrl = (url: string): string => {
   if (!url.startsWith('http://') && !url.startsWith('https://')) {
      url = 'https://' + url
   }
   if (!url.startsWith('https://www.')) {
      url = url.replace('https://', 'https://www.')
   }
   return url
}

const DashboardContent = () => {
   const [newLink, setNewLink] = useState<NewLinkState>({})
   const [editLink, setEditLink] = useState<NewLinkState>({})
   const {
      categories,
      tags,
      fetchCategories,
      fetchTags,
      addLink,
      updateLink,
      user,
   } = useStore()

   useEffect(() => {
      fetchCategories()
      fetchTags()
   }, [fetchCategories, fetchTags])

   const handleAddLink = async () => {
      if (!newLink.category) {
         console.error('Category is required.')
         return
      }
      const linkData: LinkInput = {
         url: formatUrl(newLink.url || ''),
         title: newLink.title || '',
         description: newLink.description || '',
         category: newLink.category,
         tags: newLink.tags || [],
         created_by: user?.id || 0,
      }
      console.log(linkData)
      await addLink(linkData)
      setNewLink({})
   }

   const handleUpdateLink = async () => {
      if (editLink.id && editLink.category) {
         const linkData: LinkInput = {
            id: editLink.id,
            url: formatUrl(editLink.url || ''),
            title: editLink.title || '',
            description: editLink.description || '',
            category: editLink.category,
            tags: editLink.tags || [],
            created_by: user?.id || 0,
         }
         console.log(editLink)
         await updateLink(editLink.id, linkData)
         setEditLink({})
      } else {
         console.error('ID and Category are required.')
      }
   }

   const handleCategoryChange = (e: any) => {
      setNewLink({ ...newLink, category: Number(e.target.value) })
   }

   const handleTagsChange = (selectedKeys: 'all' | Set<React.Key>) => {
      if (selectedKeys !== 'all') {
         const selectedTags = Array.from(selectedKeys).map((key) => Number(key))
         setNewLink({ ...newLink, tags: selectedTags })
         console.log(selectedTags)
      }
   }

   const handleEditCategoryChange = (e: any) => {
      setEditLink({ ...editLink, category: Number(e.target.value) })
   }

   const handleEditTagsChange = (selectedKeys: 'all' | Set<React.Key>) => {
      if (selectedKeys !== 'all') {
         const selectedTags = Array.from(selectedKeys).map((key) => Number(key))
         setEditLink({ ...editLink, tags: selectedTags })
      }
   }

   return (
      <>
         <div className="grid p-5 gap-5">
            <h2 className="text-lg font-semibold text-start">
               Управление ссылками
            </h2>
            <div className="flex flex-col lg:flex-row gap-5 w-full">
               <div className="grid space-y-3 p-3 border rounded-lg w-full lg:w-1/2">
                  <h3 className="text-md font-semibold">
                     Добавить новую ссылку
                  </h3>
                  <Input
                     fullWidth
                     label="URL"
                     value={newLink.url || ''}
                     onChange={(e) =>
                        setNewLink({ ...newLink, url: e.target.value })
                     }
                  />
                  <Input
                     fullWidth
                     label="Title"
                     value={newLink.title || ''}
                     onChange={(e) =>
                        setNewLink({ ...newLink, title: e.target.value })
                     }
                  />
                  <Textarea
                     label="Description"
                     value={newLink.description || ''}
                     onChange={(e) =>
                        setNewLink({ ...newLink, description: e.target.value })
                     }
                  />
                  <Select
                     fullWidth
                     label="Category"
                     onChange={handleCategoryChange}
                  >
                     {categories.map((category) => (
                        <SelectItem key={category.id} value={category.id}>
                           {category.name}
                        </SelectItem>
                     ))}
                  </Select>
                  <Select
                     fullWidth
                     selectionMode="multiple"
                     label="Tags"
                     onSelectionChange={handleTagsChange}
                  >
                     {tags.map((tag) => (
                        <SelectItem key={tag.id} value={tag.id}>
                           {tag.name}
                        </SelectItem>
                     ))}
                  </Select>
                  <Button onClick={handleAddLink}>Добавить</Button>
               </div>

               <div className="grid space-y-3 p-3 border rounded-lg w-full lg:w-1/2">
                  <h3 className="text-md font-semibold">
                     Редактировать ссылку
                  </h3>
                  <Input
                     fullWidth
                     label="ID"
                     value={editLink.id ? String(editLink.id) : ''}
                     onChange={(e) =>
                        setEditLink({ ...editLink, id: Number(e.target.value) })
                     }
                  />
                  <Input
                     fullWidth
                     label="URL"
                     value={editLink.url || ''}
                     onChange={(e) =>
                        setEditLink({ ...editLink, url: e.target.value })
                     }
                  />
                  <Input
                     fullWidth
                     label="Title"
                     value={editLink.title || ''}
                     onChange={(e) =>
                        setEditLink({ ...editLink, title: e.target.value })
                     }
                  />
                  <Textarea
                     label="Description"
                     value={editLink.description || ''}
                     onChange={(e) =>
                        setEditLink({
                           ...editLink,
                           description: e.target.value,
                        })
                     }
                  />
                  <Select
                     fullWidth
                     label="Category"
                     onChange={handleEditCategoryChange}
                  >
                     {categories.map((category) => (
                        <SelectItem key={category.id} value={category.id}>
                           {category.name}
                        </SelectItem>
                     ))}
                  </Select>
                  <Select
                     fullWidth
                     selectionMode="multiple"
                     label="Tags"
                     onSelectionChange={handleEditTagsChange}
                  >
                     {tags.map((tag) => (
                        <SelectItem key={tag.id} value={tag.id}>
                           {tag.name}
                        </SelectItem>
                     ))}
                  </Select>
                  <Button onClick={handleUpdateLink}>Изменить</Button>
               </div>
            </div>
         </div>
      </>
   )
}

export default DashboardContent
