import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DoctorService } from '../doctor.service';
import { ProfileService } from '../profile.service';
import { AppointmentService } from '../appointment.service';
import { PatientService } from '../patient.service';
import { Appointment } from '../models';

@Component({
  selector: 'app-appointment-details',
  templateUrl: './appointment-details.component.html',
  styleUrls: ['./appointment-details.component.css']
})
export class AppointmentDetailsComponent implements OnInit {
  appointment: Appointment | undefined;
  isAuth: boolean = false;
  errorMessage: string = '';

  constructor(
    private route: ActivatedRoute,
    private doctorService: DoctorService,
    private profileService: ProfileService,
    private router: Router,
    private appointmentService: AppointmentService,
    private patientService: PatientService
  ) { }

  ngOnInit(): void {
    this.isAuth = this.profileService.isAuthenticated();
    this.getAppointmentDetails();
  }

  getAppointmentDetails(): void {
    const profile_id = this.profileService.profileId;
    const id = Number(this.route.snapshot.paramMap.get('id'));
    if (profile_id !== null) {
      this.appointmentService.getAppointment(id, profile_id).subscribe(
        (appointment: Appointment) => {
          this.appointment = appointment;
          this.fetchDoctorDetails(appointment.doctor);
          this.fetchPatientDetails(appointment.patient);
        },
        (error) => {
          console.error('Failed to fetch appointment details', error);
          this.errorMessage = 'Failed to fetch appointment details';
        }
      );
    }
  }

  fetchDoctorDetails(doctorId: number): void {
    this.doctorService.getDoctor(doctorId).subscribe(
      (doctor: any) => {
        if (this.appointment != null) {
          this.appointment.doctor_full_name = doctor.full_name;
        }
      },
      (error) => {
        console.error('Failed to fetch doctor details', error);
        this.errorMessage = 'Failed to fetch doctor details';
      }
    );
  }

  fetchPatientDetails(patientId: number): void {
    this.patientService.getPatient(patientId).subscribe(
      (patient: any) => {
        if (this.appointment != null) {
          this.appointment.patient_full_name = patient.full_name;
        }
      },
      (error) => {
        console.error('Failed to fetch patient details', error);
        this.errorMessage = 'Failed to fetch patient details';
      }
    );
  }

  goHome(): void {
    this.router.navigate(['/']);
  }

  isFutureAppointment(appointment: Appointment): boolean {
    const now = new Date();
    const appointmentDate = new Date(appointment.date_and_time);
    return appointmentDate > now;
  }

  redirectToAppointmentEdit(): void {
    if(this.appointment && this.isFutureAppointment(this.appointment)) {
      this.router.navigate([`/doctors/${this.appointment.doctor}/appointments`], { queryParams: { appointmentId: this.appointment.id }});
    }
  }

  cancelAppointment(appointment: Appointment): void {
    if(this.profileService.profileId !== null){
      this.appointmentService.cancelAppointment(appointment, this.profileService.profileId)
        .subscribe(
          () => {
            console.log('Appointment cancelled successfully:');
            this.router.navigate(['/']); 
          },
          error => this.errorMessage = error
        );
    }
  }
}
