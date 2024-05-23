import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Specialty, Service } from './models';

@Injectable({
  providedIn: 'root',
})
export class ServiceService {
  private apiUrl = 'http://localhost:8000/api/services/';

  constructor(private http: HttpClient) {}

  getServices(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  getService(name: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}detail?name=${name}`);
  }

  getSpecialties(): Observable<Specialty[]> {
    return this.http.get<Specialty[]>('http://localhost:8000/api/specialties/');
  }

}