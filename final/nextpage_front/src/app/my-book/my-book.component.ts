import { Component, OnInit } from '@angular/core';
import { Category, CATALOG_LISTS } from '../models/category';
import { Book } from '../models/book';
import { UserlistService } from '../services/userlist.service';
import { UserList } from '../models/userlist';
@Component({
  selector: 'app-my-book',
  templateUrl: './my-book.component.html',
  styleUrls: ['./my-book.component.css']
})


export class MyBookComponent implements OnInit{
  catalog_list = CATALOG_LISTS;
  userList : UserList[];
  constructor(private userListService: UserlistService) {
    this.userList = [];
  }

  ngOnInit(): void {
    this.getUserList();
  }

  getUserList() {
    this.userListService.getUsersLists().subscribe((userList) =>{
      this.userList = userList;
      console.log(this.userList[0].books)
    })
  }
}


