import { Component } from '@angular/core';
import { Book } from '../models/book'
import { ActivatedRoute } from '@angular/router';
import { BookService } from '../services/book.service';
import { UserList } from '../models/userlist';
import { UserlistService } from '../services/userlist.service';
import { UsersService } from '../services/users.service';
import { User } from '../models/user';
@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.component.html',
  styleUrls: ['./home-page.component.css']
})
export class HomePageComponent {
    book : Book | undefined;
    id: number | undefined;
    list : Book[] = [];
    user : User | undefined;
    popular: Book[] = [];
    recommendations: Book[] = [];
    constructor(private route: ActivatedRoute, private bookService: BookService, private userList: UserlistService, private userService: UsersService){
        
    }
    ngOnInit(): void{
      this.id = Number(this.route.snapshot.paramMap.get('id'));
      this.userList.getBooksOfList('Reading').subscribe((books) => {
        if(books.length > 0){
          this.book = books[0]
        }
      }
      );
      this.getPopular();
      this.getReco();
    }
    getCur(){
      this.userList.getBooksOfList('Reading').subscribe((books) => {
        if(books != undefined && books.length != 0){
            this.book = books[0];
            console.log(this.book)
        }
      })
    }
    getPopular(){
      this.bookService.getRandomBooks().subscribe((pop) => this.popular = pop);
    }
    getReco(){
      this.bookService.getRandomBooks().subscribe((pop) => this.recommendations = pop);
    }
}
