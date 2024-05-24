import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {Router} from '@angular/router';
import {AuthService} from "../../services/auth.service";

@Component({
  selector: 'app-signup',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss'],
})
export class RegisterComponent implements OnInit {
  signupForm: FormGroup;

  constructor(
    public fb: FormBuilder,
    public authService: AuthService,
    public router: Router
  ) {
    this.signupForm = this.fb.group({
      username: [''],
      email:[''],
      password: [''],
    });
  }

  ngOnInit() {
  }

  registerUser() {
    this.authService.signUp(this.signupForm.value).subscribe((res) => {
      this.signupForm.reset();
      this.router.navigate(['auth/login']);

    });
  }
}
