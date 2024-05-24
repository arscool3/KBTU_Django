import {Component} from '@angular/core';
import {AuthService} from "../../services/auth.service";
import {HttpClient} from "@angular/common/http";
import {Router} from "@angular/router";

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.scss']
})
export class HeaderComponent {
  public check: boolean = this.authService.isLoggedIn;

  constructor(public authService: AuthService, private http: HttpClient, private router: Router) {
  }


  goToHome() {
    this.router.navigate(['/home'])

  }

  goToProducts() {
    this.router.navigate(['/products'])
  }

  goToCategories() {
    this.router.navigate(['/categories'])
  }

  goToAboutPage() {
    this.router.navigate(['/about'])
  }

  goToContactPage() {
    this.router.navigate(['/contact'])
  }

  logout() {
    this.authService.doLogout()
    this.router.navigate(['auth/login'])
  }

  login() {
    this.router.navigate(['auth/login'])
  }

  goToCorzina() {
    this.router.navigate(['corzina/'])
  }
}
