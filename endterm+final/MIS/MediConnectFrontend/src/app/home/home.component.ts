import { Component, OnInit } from '@angular/core';
import { Router, ActivatedRoute } from '@angular/router';
import { AuthService } from '../auth.service';
import { ProfileService } from '../profile.service';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrl: './home.component.css'
})

export class HomeComponent implements OnInit {
  message: string = '';

  constructor(private route: ActivatedRoute, private router: Router, private profileService: ProfileService, private authService: AuthService) { }

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.message = params['message'] || '';
    });
  }

  isAuthenticated(): boolean {
    return this.profileService.isAuthenticated();
  }

  logout(): void {
    this.authService.logout();
    window.location.reload();
  }

  goToLoginPage(): void {
    this.router.navigate(['/login']);
  }

  goToRegisterPage(): void {
    this.router.navigate(['/register']);
  }

  goToDoctors(): void {
    this.router.navigate(['/doctors']);
  }

  goToClinics(): void {
    this.router.navigate(['/clinics']);
  }

  goToServices(): void {
    this.router.navigate(['/services']);
  }
  goToProfilePage(): void {
    this.router.navigate(['/my-profile'])
  }

  goToMyAppointments(): void {
    this.router.navigate(['/my-appointments'])
  }
}
