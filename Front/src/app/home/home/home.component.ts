import {Component} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {AuthService} from "../../services/auth.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent {


  constructor(public authService: AuthService, private http: HttpClient, private router: Router) {
  }

  logout() {
    this.authService.doLogout()

  }

  protected readonly AuthService = AuthService;

  goToCategory() {
    this.router.navigate(['/categories'])
  }
}
