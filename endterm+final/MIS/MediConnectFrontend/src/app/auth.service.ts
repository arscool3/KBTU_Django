import { Injectable } from '@angular/core';
import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError, Subject } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { ProfileService } from './profile.service'; 

interface LoginResponse {
  message: string;
  profile_id: number;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private baseUrl = 'http://localhost:8000/';
  private registrationResultSubject = new Subject<string>();
  private loginResultSubject = new Subject<string>();

  registrationResult$: Observable<string> = this.registrationResultSubject.asObservable();
  loginResult$: Observable<string> = this.loginResultSubject.asObservable();

  constructor(private http: HttpClient) {}

  registerUser(first_name: string, last_name: string, email: string, password: string, role: string): void {
    const registrationUrl = `${this.baseUrl}/api/register/`;
    const user = { first_name, last_name, email, password, role };

    this.http.post(registrationUrl, user).subscribe(
      (data) => {
        console.log('Registration successful', data);
        this.registrationResultSubject.next('Registration successful');
      },
      (error) => {
        console.error('Registration failed', error);
        if (error.error && error.error.email) {
          this.registrationResultSubject.next(error.error.email[0]); 
        } else {
          this.registrationResultSubject.next('Registration failed'); 
        }
      }
    );
  }

  loginUser(email: string, password: string): void {
    const loginUrl = `${this.baseUrl}/api/login/`;
    const credentials = { email, password };

    this.http.post<LoginResponse>(loginUrl, credentials)
      .pipe(
        catchError((error: HttpErrorResponse) => {
          if (error.status === 401) {
            if (error.error.message === 'Invalid email.') {
              console.error('Invalid email');
              this.loginResultSubject.next('Invalid email');
            } else if (error.error.message === 'Invalid credentials.') {
              console.error('Incorrect password');
              this.loginResultSubject.next('Incorrect password');
            }
          }
          return throwError('Login failed');
        })
      )
      .subscribe(
        (data: LoginResponse) => {
          console.log('Login successful', data);
          const profileId = data.profile_id;
          localStorage.setItem('profile_id', profileId.toString());
          this.loginResultSubject.next('Login successful');
        }
      );
  }

  logout(): void {
    localStorage.removeItem('profile_id');
  }
  
}
