import { Injectable } from '@angular/core';
import {BehaviorSubject} from "rxjs";

@Injectable({
  providedIn: 'root'
})
export class LogService {
  constructor() { }
  error(error: any): void {
    console.error(error);
  }
}
