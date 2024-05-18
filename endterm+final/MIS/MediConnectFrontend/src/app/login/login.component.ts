import { Component } from '@angular/core';
import { AuthService } from '../auth.service';
import { Subscription } from 'rxjs';
import { ActivatedRoute } from '@angular/router';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})

export class LoginComponent {
  loginResult: string = '';
  private loginResultSubscription: Subscription| undefined;

  email: string = '';
  password: string = '';
  errorMessage: string | null = null;


  constructor(
    private authService: AuthService,
    private route: ActivatedRoute, 
    private router: Router,) {
    }

  ngOnInit(): void {
    this.errorMessage = this.route.snapshot.paramMap.get('errorMessage');
    this.loginResultSubscription = this.authService.loginResult$.subscribe(
      (result) => {
        if (result !== 'Login successful') {
          this.loginResult = result;
        } else{
          this.router.navigate(['/'], { queryParams: { message: result } });
        }
      }
    );
  }

  ngOnDestroy(): void {
    if (this.loginResultSubscription) {
      this.loginResultSubscription.unsubscribe();
    }
  }

  isValidEmail(email: string): boolean {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  }

  loginUser(): void {
    if (this.password == ''){
      this.errorMessage = 'Please fill in all fields.';
      return;
    }
    if (!this.isValidEmail(this.email)) {
      this.errorMessage = 'Please enter a valid email address.';
      return;
    } else{
      this.errorMessage = '';
    }
    this.authService.loginUser(this.email, this.password);
  }
}
