import { Component, OnInit } from '@angular/core';
import { AuthService } from '../auth.service';
import { ProfileService } from '../profile.service';
import { Profile, Specialty } from '../models';
import { Router } from '@angular/router';
import { ServiceService } from '../service.service';
import { ProfileStateService } from '../profile-state.service';


@Component({
  selector: 'app-my-profile',
  templateUrl: './my-profile.component.html',
  styleUrls: ['./my-profile.component.css']
})
export class MyProfileComponent {
  profile: Profile | null = null;
  errorMessage: string | null = null;
  isAuth: boolean = false;
  specialties: Specialty[] = []; 

  constructor(
    private profileService: ProfileService, 
    private authService: AuthService, 
    private router: Router, 
    private serviceService: ServiceService,
    private profileState: ProfileStateService
  ) { }

  ngOnInit(): void {
    this.isAuth = this.profileService.isAuthenticated()
    this.profileService.getMyProfile().subscribe(
      (profile: Profile) => {
        this.profile = profile;
        this.profileState.updateProfile(profile);  
      },
      (error) => {
        if (error === 'Profile ID is not set') {
          this.errorMessage = 'Please log in';
          this.router.navigate(['/login', { errorMessage: 'Please log in' }]);
        } else {
          this.errorMessage = 'Profile not found';
        }
      }
    );
    
    this.serviceService.getSpecialties().subscribe(
      (specialties: Specialty[]) => {
        this.specialties = specialties;
      },
      (error) => {
        console.error('Failed to fetch specialties:', error);
      }
    );
  }

  onLogoutClick(): void {
    this.authService.logout();
    window.location.reload();
  }

  goHome(): void {
    this.router.navigate(['/']);
  }

  updateProfile(): void {
    if (this.profile != null) {
      this.profileService.updateProfile(this.profile).subscribe(
        (data) => {
          console.log('Profile updated successfully', data);
        },
        (error) => {
          if (error.error && error.error.email && error.error.email.length > 0) {
            const errorMessage = error.error.email[0];
            console.error('Failed to update profile:', errorMessage);
            this.errorMessage = errorMessage;
          } else {
            console.error('Failed to update profile:', error);
          }
        }
      );
    }
  }

  goToVerification() {
    this.router.navigate(['/verify-license']);
  }
}
