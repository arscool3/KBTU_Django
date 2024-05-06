import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Doctor, Profile } from './models';
import { map } from 'rxjs/operators';


@Injectable({
  providedIn: 'root',
})

export class DoctorService {
  private apiUrl = 'http://localhost:8000/api/doctors/';

  constructor(private http: HttpClient) {}

  getDoctors(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  getDoctorIdByProfileId(profileId: number): Observable<number | null> {
    return this.http.get<Doctor[]>(`${this.apiUrl}?profile=${profileId}`).pipe(
      map(doctors => doctors.length > 0 ? doctors[0].id : null)
    );
  }
  getDoctorsBySpecialty(specialty: string): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}?specialty=${specialty}`);
  }

  getDoctor(id: number): Observable<Doctor> {
    const doctorUrl = `${this.apiUrl}${id}/`;
    return this.http.get<Doctor>(doctorUrl);
  }
  
  updateDoctor(doctorId: number, profile: any): Observable<any> {
    const doctorUrl = `${this.apiUrl}${doctorId}/`;
    const doctorData = {
      specialty: profile.specialty,
      clinic_location: profile.clinic_location,
      profile: profile.id
    };
    return this.http.put(doctorUrl, doctorData);
  }

  verifyDoctorLicense(doctorProfile: Profile): Observable<any> {
    return this.http.post('http://localhost:8000/api/verify-doctor-license', doctorProfile);
  }

}
