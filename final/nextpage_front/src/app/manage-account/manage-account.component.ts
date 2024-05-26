import {Component, OnInit} from '@angular/core';
import {User} from "../models/user";
import {UsersService} from "../services/users.service";
import {LogService} from "../services/log.service";
import {Router} from "@angular/router";

@Component({
  selector: 'app-manage-account',
  templateUrl: './manage-account.component.html',
  styleUrls: ['./manage-account.component.css']
})
export class ManageAccountComponent implements OnInit{
  errorMessage = '';
  user: User;

  constructor(private usersService: UsersService,
              private logService: LogService,
              private route: Router) {
    // @ts-ignore
    this.user = this.user;
  }

  ngOnInit(): void {
    this.getUser();
  }

  getLetter(): string {
    return this.user?.username.charAt(0).toUpperCase() || '☠';
  }

  getUser(): void {
    this.usersService.getProfile().subscribe(user => {
      this.user = user;
    }, error => {
      this.errorMessage = error.message;
      this.logService.error(error);
      setTimeout( () => this.route.navigate(['/login']), 1000);
    });
  }

  updateUser(): void {
    this.usersService.updateUser(this.user).subscribe(user => {
      this.user = user;
    }, error => {
      this.getUser();
      this.errorMessage = error.message + (error.error ? ` (${JSON.stringify(error.error)})` : '');
      this.logService.error(error);
    });
  }
}
