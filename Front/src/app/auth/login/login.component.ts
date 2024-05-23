import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup} from '@angular/forms';
import {Router} from '@angular/router';
import {AuthService} from "../../services/auth.service";
import {User} from "../../shared/user";

@Component({
  selector: 'app-signin',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent implements OnInit {
  signinForm: FormGroup;

  constructor(
    public fb: FormBuilder,
    public authService: AuthService,
    public router: Router
  ) {
    this.signinForm = this.fb.group({
      username: [''],
      password: [''],
    });
  }

  ngOnInit() {
    this.checkLogin()
  }

  checkLogin() {
    if (this.authService.isLoggedIn) {
      this.router.navigate(['/home'])
    }
  }

  loginUser() {
    this.authService.signIn(this.signinForm.getRawValue());
  }

  signUP() {
    this.router.navigate(['auth/register'])
  }
}
