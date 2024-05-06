import { Component, OnInit } from '@angular/core';
import { Appointment, Doctor, Patient } from '../models';
import { ProfileService } from '../profile.service';
import { ActivatedRoute, Router } from '@angular/router';
import { AppointmentService } from '../appointment.service';
import { DoctorService } from '../doctor.service';
import { PatientService } from '../patient.service';


@Component({
  selector: 'app-my-appointments',
  standalone: false,
  templateUrl: './my-appointments.component.html',
  styleUrl: './my-appointments.component.css'
})
export class MyAppointmentsComponent implements OnInit {
  upcomingAppointments: Appointment[] = [];
  pastAppointments: Appointment[] = [];
  activeTab: string = 'upcoming';


  constructor(
    private profileService: ProfileService,
    private router: Router,
    private appointmentService: AppointmentService,
    private route: ActivatedRoute,
    private doctorService: DoctorService,
    private patientService: PatientService
  ) {}

  ngOnInit(): void {
    if (this.profileService.isAuthenticated()) {
      if (this.profileService.profileId !== null) {
        this.appointmentService.getMyAppointments(this.profileService.profileId).subscribe(
          (appointments: Appointment[]) => {
            appointments.forEach((appointment: Appointment) => {
              this.doctorService.getDoctor(appointment.doctor).subscribe(
                (doctor: any) => {
                  appointment.doctor_full_name = doctor.full_name;
                },
                (error) => {
                  console.error('Failed to fetch doctor for appointment', error);
                }
              );
              this.patientService.getPatient(appointment.patient).subscribe(
                (patient: any) => {
                  appointment.patient_full_name = patient.full_name;
                },
                (error) => {
                  console.error('Failed to fetch doctor for appointment', error);
                }
              );
            });
            const now = new Date();
            for (const appointment of appointments) {
              const appointmentDate = new Date(appointment.date_and_time);
              if (appointmentDate > now) {
                this.upcomingAppointments.push(appointment);
              } else {
                this.pastAppointments.push(appointment);
              }
            }
          },
          (error) => {
            console.log('error', error);
          }
        )
      }
    } else{
      this.router.navigate(['/login', { errorMessage: 'Please log in' }]);
    }
  }

  viewAppointmentDetails(appointment: Appointment): void{
    this.router.navigate(['/appointment-details', appointment.id, ]);
  }

  goHome(): void {
    this.router.navigate(['/'])
  }

  setActiveTab(tab: string): void {
    this.activeTab = tab;
  }

  openTab(tabName: string) {
    this.activeTab = tabName;
  }
  
}