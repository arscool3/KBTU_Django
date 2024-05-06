import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { Subscription } from 'rxjs';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  first_name: string = '';
  last_name: string = '';
  email: string = '';
  password: string = '';
  role: string = '';
  errorMessage: string = '';
  registrationResult: string = '';
  private registrationResultSubscription: Subscription | undefined;

  constructor(private authService: AuthService) {}

  ngOnInit(): void {
    this.registrationResultSubscription = this.authService.registrationResult$.subscribe(
      (result) => {
        this.registrationResult = result;
      }
    );
  }

  ngOnDestroy(): void {
    if (this.registrationResultSubscription) {
      this.registrationResultSubscription.unsubscribe();
    }
  }

  isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  registerUser(): void {
    if(this.first_name == '' || this.last_name == '' || this.password == '' || this.role == ''){
      this.errorMessage = 'Please fill in all fields.';
      return;
    }
    if (!this.isValidEmail(this.email)) {
      this.errorMessage = 'Please enter a valid email address.';
      return;
    } else {
      this.errorMessage = '';
    }
    this.authService.registerUser(this.first_name, this.last_name, this.email, this.password, this.role);
  }
}
