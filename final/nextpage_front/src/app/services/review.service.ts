import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Review } from '../models/review';
import { Observable } from 'rxjs';
import { Rating } from '../models/rating';

@Injectable({
  providedIn: 'root'
})
export class ReviewService {

  BASE_URL = 'http://127.0.0.1:8000/api';

  constructor(private client: HttpClient) { }
  
  getReviews(id_book: number): Observable<Review[]>{
    return this.client.get<Review[]>(`${this.BASE_URL}/books/${id_book}/reviews`)
  }
  getUser(){
    return this.client.get(`${this.BASE_URL}/current_user/`)
  }
  postReview(review: string,rating:number, id_book: number, user_id: number){
    return this.client.post<Review>(`${this.BASE_URL}/books/${id_book}/reviews`,{
      review: review,rating:rating, user : user_id, book: id_book
    }).subscribe();
  } 
  getRating(id_book: number){
    return this.client.get<Rating>(`${this.BASE_URL}/books/${id_book}/rating`)
  }
}
