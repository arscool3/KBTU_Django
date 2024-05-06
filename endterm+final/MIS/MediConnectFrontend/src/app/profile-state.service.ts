import { Injectable } from '@angular/core';
import { BehaviorSubject, Observable } from 'rxjs';
import { Profile } from './models'; 

@Injectable({
  providedIn: 'root'
})
export class ProfileStateService {
  private profileSource = new BehaviorSubject<Profile | null>(null);
  currentProfile = this.profileSource.asObservable();

  constructor() { }

  updateProfile(profile: Profile): void {
    this.profileSource.next(profile);
  }

  clearProfile(): void {
    this.profileSource.next(null);
  }
}
