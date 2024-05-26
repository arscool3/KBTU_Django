import { Component, OnInit } from '@angular/core';
import { User } from '../models/user';
import { ActivatedRoute, Router } from '@angular/router';
import { UsersService } from '../services/users.service';
import 'jqueryui';
import { LogService } from '../services/log.service';
import { UserlistService } from '../services/userlist.service';
declare var $: any;

@Component({
  selector: 'app-profile-page',
  templateUrl: './profile-page.component.html',
  styleUrls: ['./profile-page.component.css']
})
export class ProfilePageComponent implements OnInit{
  findUser : string = '';
  cur = 0;
  alr = 0;
  wil = 0;
  id = 0;
  users : User[] = []
      constructor(private usersService: UsersService, private logService: LogService, private route: Router,private routed: ActivatedRoute,private userList: UserlistService) {
    // @ts-ignore
    this.user = this.user;
    }
    
    ngOnInit(): void {
      this.routed.paramMap.subscribe((params) => {
        this.id = Number(params.get('id'));
        if (this.id != 0){
          // console.log(this.id)
          
          this.getOtherUser(this.id)
          this.getUserInfo(this.id);
        }
        if (this.id  == 0){
          // this.home = true;
          this.getUser();
          this.getRead()
          this.getAlr();
          this.getWill();
        }
      })
      // this.getRead()
      // this.getAlr();
      // this.getWill();
      $('#search').autocomplete({
        source: (request: { term: string; }, response: (arg0: User[]) => void) => {
          this.usersService.getFindUsers(request.term).subscribe(data => {
            response(data.filter((user) => user.username.toLowerCase().startsWith(this.findUser.toLowerCase())));
          });
        },
        minLength: 3,
        select: (ui: { item: { username: string; }; }) => {
          this.findUser = ui.item.username;
        }
      });
    }
  getUserInfo(user_id:number){
    this.userList.getBooksOfOther('Read',user_id).subscribe((alr) => 
    {
      if(alr != undefined){
        this.alr = alr.length;
      }
      else{
        this.alr = 0
      }
    });
    this.userList.getBooksOfOther('Reading',user_id).subscribe((alr) => 
    {
      if(alr != undefined){
        this.cur = alr.length;
        console.log(alr)
      }
      else{
        this.cur = 0
      }
    });
    this.userList.getBooksOfOther('Planned',user_id).subscribe((alr) => 
    {
      if(alr != undefined){
        this.wil = alr.length;
      }
      else{
        this.wil = 0
      }
    });
  }
  errorMessage = '';
  user: User;
  getLetter(): string {
    return this.user?.username.charAt(0).toUpperCase() || '☠';
  }
  getRead(){
    this.usersService.getUserListBooks('Reading').subscribe((read) => {
      if(read.length != undefined){
        this.cur = read.length
      }});
  }
  getAlr(){
    this.usersService.getUserListBooks('Read').subscribe((read) => {
      if(read.length != undefined){
        this.alr = read.length
      }});
  }
  getWill(){
    this.usersService.getUserListBooks('Planned').subscribe((read) => {
      if(read.length != undefined){
        this.wil = read.length
      }});
  }
  getOtherUser(id: number){
    this.usersService.getUserById(id).subscribe((user) => this.user = user);
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
  changeUser(user_id: number){
    console.log(user_id);
    this.getOtherUser(user_id);
    this.getUserInfo(user_id);
    console.log(this.alr)
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
    myProfile = false;
    search() {
      this.usersService.getFindUsers(this.findUser).subscribe((data) => {
        this.users = data;
      });
    }
}
