import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DoctorService } from '../doctor.service';
import { ProfileService } from '../profile.service';
import { AppointmentService } from '../appointment.service';
import { Appointment, Doctor } from '../models';
import { PatientService } from '../patient.service';

@Component({
  selector: 'app-appointment',
  templateUrl: './appointment.component.html',
  styleUrls: ['./appointment.component.css']
})
export class AppointmentComponent implements OnInit {
  isEditMode: boolean = false;
  availableSlots: Date[] = [];
  selectedSlotDate: Date | null = null;
  doctor_id: number = -1;
  doctorProfileId: number | null = null;
  errorMessage: string = '';
  message: string = '';
  days: string[] = [];
  hours: string[] = [];
  appointment: Appointment | null = null;

  constructor(
    private profileService: ProfileService,
    private router: Router,
    private appointmentService: AppointmentService,
    private route: ActivatedRoute,
    private doctorService: DoctorService,
    private patientService: PatientService
  ) {}

  ngOnInit(): void {
    this.route.queryParams.subscribe(params => {
      this.isEditMode = !!params['appointmentId'];
      this.doctor_id = +this.route.snapshot.paramMap.get('id')!;
      if (!this.profileService.isAuthenticated()) {
        this.router.navigate(['/login'], { queryParams: { errorMessage: 'Please log in' }});
        return;
      }
      if (this.isEditMode && params['appointmentId']) {
        this.loadExistingAppointment(params['appointmentId']);
      }
      this.loadAvailableSlots();
    });
    this.days = this.getDaysOfWeek();
    this.hours = this.getHoursOfDay();
  }

  loadExistingAppointment(appointmentId: string): void {
    const numericAppointmentId = Number(appointmentId);
    if (!isNaN(numericAppointmentId) && this.profileService.profileId !== null) {
      this.appointmentService.getAppointment(numericAppointmentId, this.profileService.profileId).subscribe(appointment => {
        this.appointment = appointment;
        this.selectedSlotDate = new Date(appointment.date_and_time);
        this.doctorProfileId = appointment.doctorId;
      });
    }
  }

  loadAvailableSlots(): void {
    this.doctorService.getDoctor(this.doctor_id).subscribe(
      (doctor: Doctor) => {
        this.doctorProfileId = doctor.profile;
        if (this.profileService.profileId !== null) {
          this.appointmentService.getDoctorAppointmentsSlots(this.profileService.profileId, this.doctorProfileId).subscribe(
            (data: any) => {
              this.availableSlots = data.available_slots.map((slot: string) => new Date(slot));
            },
            (error) => {
              console.error('Failed to fetch appointments slots:', error);
            }
          );
        }
      }
    );
  }

  getDaysOfWeek(): string[] {
    const today = new Date();
    const tomorrow = new Date(today.getTime() + 24 * 60 * 60 * 1000); 
    const days = [];
    for (let i = 0; i < 7; i++) {
      const nextDay = new Date(tomorrow.getTime() + i * 24 * 60 * 60 * 1000);
      if (nextDay.getDay() !== 0 && nextDay.getDay() !== 6) {
        days.push(`${nextDay.getDate()} ${nextDay.toLocaleDateString('en-US', { month: 'short' })}`);
      }
    }
    return days;
  }

  getHoursOfDay(): string[] {
    const hours = [];
    for (let i = 9; i < 18; i++) {
      if (i != 13){
        hours.push(`${i % 12 === 0 ? 12 : i % 12}:00 ${i < 12 ? 'AM' : 'PM'}`);
      }
    }
    return hours;
  }

  isSlotAvailable(day: string, hour: string): boolean {
    const today = new Date();
    const currentYear = today.getFullYear();
    const slotDate = new Date(`${currentYear}-${day}T${hour}`);
    return this.availableSlots.some(slot => slot.getTime() === slotDate.getTime());
  }

  isSelectedSlot(day: string, hour: string): boolean {
    const today = new Date();
    const currentYear = today.getFullYear();
    const slotDate = new Date(`${currentYear}-${day}T${hour}`);
    if (this.selectedSlotDate !== null) {
      return this.selectedSlotDate.getTime() === slotDate.getTime();
    }
    return false;
  }

  selectSlot(day: string, hour: string): void {
    const today = new Date();
    const currentYear = today.getFullYear();
    const slotDate = new Date(`${currentYear}-${day}T${hour}`);
    if (this.isSlotAvailable(day, hour)) {
      this.selectedSlotDate = slotDate;
    }
  }


  scheduleAppointment(): void {
    if (!this.selectedSlotDate) {
      this.errorMessage = 'No slot selected';
      return;
    }
    if (this.profileService.profileId !== null) {
    this.patientService.getPatientIdByProfileId(this.profileService.profileId).subscribe({
      next: (patientId) => {
        let appointmentData = {
          doctor: this.doctor_id,
          patient: patientId,
          date_and_time: this.selectedSlotDate
        };
    
        if(this.profileService.profileId !== null && this.doctorProfileId !== null){
          if (this.isEditMode && this.appointment !== null) {
            this.appointmentService.updateAppointment(this.appointment, appointmentData, this.profileService.profileId).subscribe(() => {
              this.message = 'Appointment updated successfully';
              this.router.navigate(['/']);
            });
          } else {
            this.appointmentService.scheduleAppointment(this.profileService.profileId, this.doctorProfileId, appointmentData).subscribe(() => {
              this.message = 'Appointment created successfully';
              this.router.navigate(['/']);
            });
          }
       }
      },
      error: (error) => {
        console.error('Failed to fetch patient ID:', error.message);
      }
    });
  } else {
    this.router.navigate(['/login'], { queryParams: { errorMessage: 'Please log in' }});
    return;
  }
    
  }

  goHome(): void {
    this.router.navigate(['/']);
  }
}
