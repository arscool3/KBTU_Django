import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import { UserList } from '../models/userlist';
import { Book, Book2 } from '../models/book';
@Injectable({
  providedIn: 'root'
})
export class UserlistService {

  BASE_URL = 'http://127.0.0.1:8000/api';

  constructor(private client: HttpClient) { }
  
  getUsersLists(): Observable<UserList[]>{
    return this.client.get<UserList[]>(`${this.BASE_URL}/list`)
  }

  getBooksOfList(name: string): Observable<Book[]>{
    return this.client.get<Book[]>(`${this.BASE_URL}/list/${name}/books`)
  }

 
  postBookToList(listName:string, book: Book2): Observable<UserList>{
    return this.client.post<UserList>(`${this.BASE_URL}/list/${listName}/books/`, book)
  }
 
  deletetBookFromList(listName: string, book: Book2): Observable<UserList> {
    return this.client.delete<UserList>(`${this.BASE_URL}/list/${listName}/books/`, { body: book, responseType: 'json' });
  }
  getListOfBook(id: number): Observable<UserList[]>{
    return this.client.get<UserList[]>(`${this.BASE_URL}/lists/book/${id}/`)
  }

  
  getBooksOfOther(listname:string, user_id: number): Observable<UserList[]>{
    return this.client.get<UserList[]>(`${this.BASE_URL}/list/${listname}/books/${user_id}/`)
  }
  
  

  
}
