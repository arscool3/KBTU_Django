import { Component, OnInit } from '@angular/core';
import { ProfileStateService } from '../profile-state.service';  
import { Profile } from '../models';
import { DoctorService } from '../doctor.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-doctor-verification',
  templateUrl: './doctor-verification.component.html',
  styleUrls: ['./doctor-verification.component.css']
})
export class DoctorVerificationComponent implements OnInit {
  doctorProfile: Profile | null = null;

  constructor(
    private profileState: ProfileStateService,
    private doctorService: DoctorService,
    private router: Router,  
  ) { }

  ngOnInit(): void {
    this.profileState.currentProfile.subscribe(profile => {
      this.doctorProfile = profile;
    });
  }

  submitLicenseInfo(): void {
    if (this.doctorProfile) {
      this.doctorService.verifyDoctorLicense(this.doctorProfile).subscribe({
        next: (response) => {
          console.log('Verification submitted', response);
          alert('License information submitted for verification.');
          this.router.navigate(['/my-profile']); 
        },
        error: (error) => {
          console.error('Error submitting verification', error);
          alert('Failed to submit license information.');
        }
      });
    }
  }

}

