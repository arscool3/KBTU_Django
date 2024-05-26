import {Component, OnInit} from '@angular/core';
import {UsersService} from '../services/users.service';
import {LogService} from '../services/log.service';
import {Router} from '@angular/router';



@Component({
  selector: 'app-sign-in-page',
  templateUrl: './sign-in-page.component.html',
  styleUrls: ['./sign-in-page.component.css']
})
export class SignInPageComponent implements OnInit{
  username :string  = '';
  password :string = '';
  constructor(private usersService: UsersService,
              private logService: LogService,
              private route: Router) {
  }

  ngOnInit(): void {
    this.checkUser();
  }

  checkUser(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.route.navigate(['/home']);
    }
  }

  login(): void{
    this.password = this.password.trim();
    this.username = this.username.trim();
    if (!(this.username && this.password)) {
      window.alert('Password and username shouldn\'t be empty!');
      return;
    }

    this.usersService.login(this.username, this.password).subscribe((data) => {
      localStorage.setItem('token', data.token);
      this.username = '';
      this.password = '';
      location.reload();
    }, error => {
      this.logService.error(error);
      window.alert('Invalid credentials!');
    });
  }

}
