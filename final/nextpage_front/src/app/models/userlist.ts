import { Book } from "./book";
import { User } from "./user";

export interface UserList{
        name: string;
        user: User;
        books: Book[];
}