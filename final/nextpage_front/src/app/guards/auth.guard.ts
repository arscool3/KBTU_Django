import { Injectable } from '@angular/core';
import {ActivatedRouteSnapshot, CanActivate, Router, RouterStateSnapshot, UrlTree} from '@angular/router';
import {Observable, tap} from 'rxjs';
import {UsersService} from "../services/users.service";
import {LogService} from "../services/log.service";
import {AuthService} from "../services/auth.service";

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(private auth: AuthService, private router: Router) {
  }
  canActivate(){
    if (this.auth.IsLoggedIn()){
      return true;
    }
    this.router.navigate(['signin']);
    return false;
  }

}
