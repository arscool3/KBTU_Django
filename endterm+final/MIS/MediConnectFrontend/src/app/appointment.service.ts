import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, mergeMap, of, throwError } from 'rxjs';
import { ProfileService } from './profile.service';
import { Appointment, Profile } from './models';
import { switchMap, catchError } from 'rxjs/operators';



@Injectable({
  providedIn: 'root'
})

export class AppointmentService {

  private apiUrl = 'http://localhost:8000/api/doctors/';
  private apiPatientUrl = 'http://localhost:8000/api/patients/';
  private apiAppUrl = 'http://localhost:8000/api/appointments/';

  constructor(private http: HttpClient, private profileService: ProfileService) { }

  getDoctorAppointments(profileId: number, doctorId: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}${doctorId}/appointments/?profile_id=${profileId}`);
  }

  getDoctorAppointmentsSlots(profileId: number, doctorprofileId: number): Observable<any> {
    let params = new HttpParams()
    params = params.append('slots', 'true');
    return this.http.get<any>(`http://localhost:8000/api/doctor-appointments/${doctorprofileId}/?profile_id=${profileId}`, {params});
  }

  scheduleAppointment(profileId: number, doctorprofileId: number, appointmentData: any): Observable<any> {
    return this.http.post<any>(`http://localhost:8000/api/doctor-appointments/${doctorprofileId}/?profile_id=${profileId}`, appointmentData);
  }

  getMyAppointments(profileId: number): Observable<any> {
    return this.profileService.getProfile(profileId).pipe(
      mergeMap((profile: Profile) => {
        if (profile.is_doctor) {
          this.http.get<any>(`${this.apiUrl}`).subscribe(
            (data: any) => {
          console.log("have: ", data);
            }
          )
          return this.http.get<any>(`http://localhost:8000/api/doctor-appointments/${profileId}/?profile_id=${profileId}`);
        } else {
          return this.http.get<any>(`${this.apiPatientUrl}${profileId}/appointments?profile_id=${profileId}`);
        }
      })
    );
  }

  getAppointment(id: number, profileId: number): Observable<any> {
    return this.http.get<any>(`${this.apiAppUrl}${id}/?profile_id=${profileId}`);
  }

  updateAppointment(appointment: Appointment, updateData: any, profile_id: number): Observable<any> {
    const updateUrl = `http://localhost:8000/api/doctor-appointments/${updateData.doctor}/detail/${appointment.id}/?profile_id=${profile_id}`;
    
    return this.http.put(updateUrl, updateData).pipe(
        catchError(err => {
            console.error('Failed to update appointment:', err);
            return throwError(() => err);
        })
    );
}

  update(id: number, profileId: number): Observable<any> {
    return this.http.get<any>(`${this.apiAppUrl}${id}/?profile_id=${profileId}`);
  }

  updateGoogleMeetLink(appointmentId: number, googleMeetLink: string) {
    const url = `${this.apiAppUrl}${appointmentId}/update-google-meet-link/`;
    const body = { google_meet_link: googleMeetLink };

    return this.http.patch(url, body);
  }

  cancelAppointment(appointment: Appointment, profile_id: number): Observable<any> {
    return this.profileService.getProfileIdByDoctorId(appointment.doctor).pipe(
      switchMap(doctor_profile_id => {
        if (!doctor_profile_id) {
          return throwError(() => new Error('Profile ID not found'));
        }
        console.log('Received profile ID:', doctor_profile_id);
        const deleteUrl = `http://localhost:8000/api/doctor-appointments/${doctor_profile_id}/detail/${appointment.id}/?profile_id=${profile_id}`;
        return this.http.delete(deleteUrl);
      }),
      catchError(err => {
        console.error('Failed to get or delete profile ID:', err);
        return throwError(() => err);
      })
    );
  }
  
}
