import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import {Observable} from "rxjs";
import { Category } from '../models/category';

@Injectable({
  providedIn: 'root'
})
export class CategoryService {

  BASE_URL = 'http://127.0.0.1:8000/api';

  constructor(private client: HttpClient) { }
  
  getCategories(): Observable<Category[]>{
    return this.client.get<Category[]>(`${this.BASE_URL}/categories`)
  }


  getCategory(category_id:number): Observable<Category>{
    return this.client.get<Category>(`${this.BASE_URL}/categories/${category_id}`)
  }


}
