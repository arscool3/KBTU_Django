import { Component, OnInit, Input } from '@angular/core';
import { DoctorService } from '../doctor.service';
import { CommonModule } from '@angular/common';
import { Profile, Doctor, Appointment } from '../models';
import { ProfileService } from '../profile.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-doctors',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './doctors.component.html',
  styleUrl: './doctors.component.css'
})

export class DoctorsComponent implements OnInit {
  @Input() specialty: string | null = null;
  doctors: Doctor[] = [];

  constructor(
    private doctorService: DoctorService,
    private profileService: ProfileService,
    private router: Router,
  ) {}

  ngOnInit(): void {
    if (this.specialty) {
      this.fetchDoctorsBySpecialty(this.specialty);
    } else {
      this.fetchAllDoctors();
    }
  }

  private fetchDoctorsBySpecialty(specialty: string): void {
    this.doctorService.getDoctorsBySpecialty(specialty).subscribe(
      (doctors: Doctor[]) => {
        this.processDoctors(doctors);
      },
      (error) => {
        console.error('Failed to fetch doctors by specialty', error);
      }
    );
  }

  private fetchAllDoctors(): void {
    this.doctorService.getDoctors().subscribe(
      (doctors: Doctor[]) => {
        this.processDoctors(doctors);
      },
      (error) => {
        console.error('Failed to fetch doctors', error);
      }
    );
  }

  private processDoctors(doctors: Doctor[]): void {
    doctors.forEach((doctor: Doctor) => {
      this.profileService.getProfile(doctor.profile).subscribe(
        (profile: any) => {
          doctor.first_name = profile.first_name;
          doctor.lastName = profile.last_name;
          doctor.email = profile.email;
          this.doctors.push(doctor);
        },
        (error) => {
          console.error('Failed to fetch profile for doctor', error);
        }
      );
    });
  }


  viewDoctorDetails(doctor: Doctor): void {
    this.router.navigate(['/doctors', doctor.id]);
  }

  goHome(): void {
    this.router.navigate(['/']);
  }

}
