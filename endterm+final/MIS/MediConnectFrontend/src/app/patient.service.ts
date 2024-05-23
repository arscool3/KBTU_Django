import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, map, throwError } from 'rxjs';
import { Patient } from './models'

@Injectable({
  providedIn: 'root',
})
export class PatientService {
  private apiUrl = 'http://localhost:8000/api/patients/';

  constructor(private http: HttpClient) {}

  getPatients(): Observable<any[]> {
    return this.http.get<any[]>(this.apiUrl);
  }

  getPatient(id: number): Observable<Patient> {
    const Url = `${this.apiUrl}${id}/`;
    return this.http.get<Patient>(Url);
  }

  getPatientIdByProfileId(profileId: number): Observable<number> {
    const url = `${this.apiUrl}profile_id/${profileId}/`;
    return this.http.get<{patient_id: number}>(url).pipe(
      map(response => response.patient_id),
      catchError(error => throwError(() => new Error(`Error fetching patient ID: ${error.message}`)))
    );
  }

}
