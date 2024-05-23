import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { DoctorService } from '../doctor.service';
import { ProfileService } from '../profile.service';
import { AppointmentService } from '../appointment.service';
import { Appointment, Doctor, EventResponse, Profile } from '../models';
import { PatientService } from '../patient.service';
import { v4 as uuidv4 } from 'uuid';
import { HttpClient } from '@angular/common/http';
import { OAuthService, AuthConfig } from 'angular-oauth2-oidc';
import { forkJoin } from 'rxjs';

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
  appointmentId: number | null = null;
  patientEmail: string = '';
  doctorEmail: string = '';

  constructor(
    private profileService: ProfileService,
    private router: Router,
    private appointmentService: AppointmentService,
    private route: ActivatedRoute,
    private doctorService: DoctorService,
    private patientService: PatientService,
    private http: HttpClient,
    private oauthService: OAuthService
  ) {
  }

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
          if (this.profileService.profileId !== null && this.doctorProfileId !== null) {
            const doctorId = this.doctorProfileId;
            let appointmentData = {
              doctor: this.doctor_id,
              patient: patientId,
              date_and_time: this.selectedSlotDate
            };
  
            if (this.isEditMode && this.appointment !== null) {
              this.appointmentService.updateAppointment(this.appointment, appointmentData, this.profileService.profileId).subscribe((appointment) => {
                this.appointmentId = appointment.id;
                this.message = 'Appointment updated successfully';
              });
            } else {
              this.appointmentService.scheduleAppointment(this.profileService.profileId, this.doctorProfileId, appointmentData).subscribe((appointment) => {
                this.appointmentId = appointment.id;
                this.message = 'Appointment created successfully';
              });
            }
            this.createGoogleMeetEvent(appointmentData);
          }
        },
        error: (error) => {
          console.error('Failed to fetch patient ID:', error.message);
        }
      });
    } else {
      console.error('Profile ID or Doctor ID is null');
      this.router.navigate(['/login'], { queryParams: { errorMessage: 'Please log in' }});
    }
  }  
  

  createGoogleMeetEvent(appointmentData: any): void {
    if (this.profileService.profileId !== null && this.doctorProfileId !== null) {
      forkJoin([
        this.profileService.getProfile(this.profileService.profileId),
        this.profileService.getProfile(this.doctorProfileId)
      ]).subscribe(
        ([patientProfile, doctorProfile]) => {
          const eventData = {
            summary: 'Appointment with ' + appointmentData.doctor,
            location: 'Google Meet',
            description: 'Consultation via Google Meet.',
            start: {
              dateTime: appointmentData.date_and_time,
              timeZone: 'Asia/Almaty'
            },
            end: {
              dateTime: new Date(appointmentData.date_and_time.getTime() + 30 * 60000).toISOString(),
              timeZone: 'Asia/Almaty'
            },
            attendees: [
              { email: patientProfile.email },
              { email: doctorProfile.email }
            ],
            conferenceData: {
              createRequest: {
                requestId: uuidv4(),
                conferenceSolutionKey: {
                  type: 'hangoutsMeet'
                }          
              }
            }
          };
    
          this.http.post<EventResponse>('https://www.googleapis.com/calendar/v3/calendars/primary/events', eventData, {
            params: {
              conferenceDataVersion: '1'
            },
            headers: {
              Authorization: `Bearer ${this.oauthService.getAccessToken()}`
            }
          }).subscribe(response => {
            console.log('Google Meet event created:', response);
            this.message += ' and Google Meet link created.';
            if (response.conferenceData && response.conferenceData.entryPoints) {
              const googleMeetLink = response.conferenceData.entryPoints[0]?.uri;
              if (googleMeetLink) {
                if (this.appointmentId !== null){
                  this.updateGoogleMeetLink(this.appointmentId, googleMeetLink)
                }

              }
            } else {
              console.error('No conference data found in response');
            }
            
            this.router.navigate(['/']);
          }, error => {
            console.error('Error creating Google Meet event', error);
            this.errorMessage = 'Failed to create Google Meet link';
          });
        }, error => {
          console.error('Failed to get profiles:', error);
        }
      );
    }
  }
  
  updateGoogleMeetLink(appointmentId: number, googleMeetLink: string) {
    this.appointmentService.updateGoogleMeetLink(appointmentId, googleMeetLink)
      .subscribe(
        response => {
          console.log('Google Meet link updated successfully:', response);
        },
        error => {
          console.error('Failed to update Google Meet link:', error);
        }
      );
  }
  
  goHome(): void {
    this.router.navigate(['/']);
  }
}
