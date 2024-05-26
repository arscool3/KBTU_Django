import { Component, Input, OnInit } from '@angular/core';
import { UserList } from '../models/userlist';
import { UserlistService } from '../services/userlist.service';
import { ActivatedRoute } from '@angular/router';
import { Book } from '../models/book';
@Component({
  selector: 'app-user-list',
  templateUrl: './user-list.component.html',
  styleUrls: ['./user-list.component.css']
})
export class UserListComponent implements OnInit{
  @Input() list: UserList ;
  books : Book[] | undefined;

  constructor(private userListService: UserlistService, ) {
    this.list = {} as UserList;
    
    // this.books = this.list.books
  }
  ngOnInit(): void {
    this.getBooksOfList();
  }
  
  
  getBooksOfList() {
    this.userListService.getBooksOfList(this.list.name).subscribe((books) =>{
      this.books = books;
    })
  }
}
