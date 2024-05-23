import { Component, OnInit } from '@angular/core';
import { Doctor, Profile, Appointment } from '../models';
import { DoctorService } from '../doctor.service';
import { ActivatedRoute } from '@angular/router';
import { ProfileService } from '../profile.service';
import { Router } from '@angular/router';
import { AppointmentService } from '../appointment.service';

@Component({
  selector: 'app-doctor',
  templateUrl: './doctor.component.html',
  styleUrl: './doctor.component.css'
})
export class DoctorComponent implements OnInit{
  doctor: Doctor | undefined;
  appointments: Appointment[] = []; 
  isAuth: boolean = false;
  errorMessage: String = '';

  constructor(
    private route: ActivatedRoute,
    private doctorService: DoctorService,
    private profileService: ProfileService,
    private router: Router,
    private appointmentService: AppointmentService
  ) { }

  ngOnInit(): void {
    this.getDoctorDetails();
    this.isAuth = this.profileService.isAuthenticated();
  }

  getDoctorDetails(): void {
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.doctorService.getDoctor(id).subscribe(doctor => {
        this.profileService.getProfile(doctor.profile).subscribe(
          (profile: Profile) => {
            doctor.first_name = profile.first_name;
            doctor.lastName = profile.last_name;
            doctor.email = profile.email;
          },
          (error) => {
            console.error('Failed to fetch profile for doctor', error);
          }
        );
        this.doctor = doctor;
      }
    );
  }

  goHome() : void {
    this.router.navigate(['/']);
  }

  scheduleAppointment(doctorId: number): void {
    if (this.isAuth) {
      if (this.profileService.profileId !== null) {
        this.profileService.getMyProfile().subscribe(profile => {
          if (profile && !profile.is_doctor) {
            this.router.navigate([`/doctors/${doctorId}/appointments`]);
          } else {
            this.errorMessage = 'Doctors are not allowed to schedule appointments.'
          }
        });        
        
      }
    } else{
      this.router.navigate(['/login', { errorMessage: 'Please log in' }]);
    }
  }
}
