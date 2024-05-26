import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Book } from '../models/book';

@Injectable({
  providedIn: 'root'
})
export class BookService {

  BASE_URL = 'http://127.0.0.1:8000/api';

  constructor(private client: HttpClient) { }
  
  getBooks(): Observable<Book[]>{
    return this.client.get<Book[]>(`${this.BASE_URL}/books`)
  }
  getFindBooks(query: string): Observable<Book[]> {
    return this.client.get<Book[]>(`${this.BASE_URL}/search/${query}/`);
  }
  getBooksByCategory(category_id: Number): Observable<Book[]>{
    return this.client.get<Book[]>(`${this.BASE_URL}/categories/${category_id}/books`)
  }
  getRandomBooks(): Observable<Book[]>{
    return this.client.get<Book[]>(`${this.BASE_URL}/books/popular`)
  }
  getBookById(id: number): Observable<Book>{
    return this.client.get<Book>(`${this.BASE_URL}/books/${id}/`)
  }
}
