// core/interfaces.ts
export interface User {
  id: number;
  username: string;
  email: string;
  isAdminUser: boolean;  // Ensure this field is included
}

export interface Category {
   id: number
   name: string
}

export interface Tag {
   id: number
   name: string
}

export interface Link {
   id: number
   url: string
   title: string
   description: string
   category: Category
   created_by: User
   tags: Tag[]
}

export interface LinkInput {
   id?: number
   url: string
   title: string
   description?: string
   category?: number
   tags?: number[]
   created_by?: number
}

export interface Click {
   id: number
   link: number
   timestamp: string
}

export interface LinkUsage {
   id: number
   link: Link
   clicks: number
}
