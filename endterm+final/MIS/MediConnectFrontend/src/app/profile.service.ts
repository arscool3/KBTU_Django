import { Injectable } from '@angular/core';
import { Profile } from './models';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError, of, forkJoin } from 'rxjs';
import { DoctorService } from './doctor.service';
import { mergeMap, catchError, filter, map, switchMap } from 'rxjs/operators';
import { error } from 'console';



@Injectable({
  providedIn: 'root'
})
export class ProfileService {
    baseUrl = 'http://localhost:8000/api';
    profileId: number | null = null;
    
    constructor(private http: HttpClient, private doctorService: DoctorService) { }

    isAuthenticated(): boolean {
      let st_profile_id = localStorage.getItem('profile_id')
      if (st_profile_id !== null) {
        this.profileId = parseInt(st_profile_id)
      }
      return this.profileId !== null;
    }
  
    getMyProfile(): Observable<Profile> {
      if (this.profileId === null) {
        return throwError('Profile ID is not set');
      }
      const profileUrl = `${this.baseUrl}/profiles/${this.profileId}/`;

      return this.http.get<Profile>(profileUrl).pipe(
        mergeMap(profile => {
          if (profile === undefined) {
            return throwError('Profile is undefined');
          }
    
          if (this.profileId === null) {
            return throwError('Profile ID is not set');
          }
    
          if (!profile.is_doctor) {
            return of(profile);
          }
          return this.doctorService.getDoctorIdByProfileId(this.profileId).pipe(
            mergeMap(doctorId => {
              if (doctorId === null) {
                return throwError('Doctor ID not found');
              }
    
              return this.doctorService.getDoctor(doctorId).pipe(
                mergeMap(doctor => {
                  profile.specialty = doctor.specialty ?? undefined;
                  profile.clinic_location = doctor.clinic_location ?? '';
                  profile.license_status = doctor.license_status ?? undefined;
                  return of(profile);
                })
              );
            })
          );
        }),
        catchError(error => {
          console.error('Error fetching profile', error);
          return throwError(error);
        }),
        filter(profile => profile !== undefined)
      );
    }

    getProfile(profileId: number): Observable<Profile> {
      const url = `${this.baseUrl}/profiles/${profileId}/`;
      return this.http.get<Profile>(url);
    }

    updateProfile(profile: Profile): Observable<any> {
      const profileurl = `${this.baseUrl}/profiles/`
      if (profile.is_doctor) {
        return this.doctorService.getDoctorIdByProfileId(profile.id).pipe(
          mergeMap(doctorId => {
            if (doctorId === null) {
              throw new Error('Doctor ID not found');
            }
            const updateProfileRequest = this.http.put(`${profileurl}${profile.id}/`, profile);
            const updateDoctorRequest = this.doctorService.updateDoctor(doctorId, profile);
            return forkJoin([updateProfileRequest, updateDoctorRequest]);
          })
        );
      } else {
        return this.http.put(`${profileurl}${profile.id}/`, profile);
      }
    }

    getProfileIdByDoctorId(doctorId: number): Observable<number> {
      const url = `${this.baseUrl}/doctor_profile_id/${doctorId}/`;
      return this.http.get<{profile_id: number}>(url).pipe(
        map(response => response.profile_id),
        catchError(error => throwError(error))
      );
    }
    
}
