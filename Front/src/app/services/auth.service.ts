import {Injectable} from '@angular/core';
import {Observable, throwError} from 'rxjs';
import {catchError, map} from 'rxjs/operators';
import {
  HttpClient,
  HttpHeaders,
  HttpErrorResponse,
} from '@angular/common/http';
import {Router} from '@angular/router';
import {User} from "../shared/user";

@Injectable({
  providedIn: 'root',
})
export class AuthService {
  endpoint: string = 'http://localhost:8000/';
  headers = new HttpHeaders().set('Content-Type', 'application/json');
  currentUser = {};

  constructor(private http: HttpClient, public router: Router) {
  }


  signUp(user: User): Observable<any> {
    let api = `${this.endpoint}api/register/`;
    return this.http.post(api, user).pipe(catchError(this.handleError));
  }


  signIn(data: any) {
    return this.http
      .post<any>(`${this.endpoint}login/`, data)
      .subscribe((res: any) => {
        localStorage.setItem('access_token', res.access);
        this.router.navigate(['home/'])
      });
  }

  getToken() {
    return localStorage.getItem('access_token');
  }

  get isLoggedIn(): boolean {
    let authToken = localStorage.getItem('access_token');
    return authToken !== null;
  }

  doLogout() {
    localStorage.removeItem('access_token');
    if (!this.isLoggedIn) {
      this.router.navigate(['auth/Login']);
    }
  }

  // Error
  handleError(error: HttpErrorResponse) {
    let msg = '';
    if (error.error instanceof ErrorEvent) {
      // client-side error
      msg = error.error.message;
    } else {
      // server-side error
      msg = `Error Code: ${error.status}\nMessage: ${error.message}`;
    }
    return throwError(msg);
  }
}
