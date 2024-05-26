import { Component } from '@angular/core';
import {Router} from '@angular/router';

import { Book } from '../models/book';

import { BookService } from '../services/book.service';
import {User} from "../models/user";
import 'jqueryui';
declare var $: any;

@Component({
  selector: 'app-top-bar',
  templateUrl: './top-bar.component.html',
  styleUrls: ['./top-bar.component.css']
})

export class TopBarComponent {
  
    check = false;
    findBook : string = '';
    books : Book[] | undefined;
    // constructor(private bookService: bookService){
    user: User;
    // }
    showBar(){
      this.check = !this.check;
    }
    // addCompany(){
    //   this.bookService.findBook(this.findBook).subscribe((book) => {
    //     if(book.name == this.findBook){

    //     }
    //   })
    // }
  logged = false;
  constructor(private route: Router,private bookService: BookService) {
    // @ts-ignore
    this.user = this.user;

  }
  ngOnInit(): void {
    this.loadUser();
    $('#search').autocomplete({
      source: (request: { term: string; }, response: (arg0: Book[]) => void) => {
        this.bookService.getFindBooks(request.term).subscribe(data => {
          response(data.filter((book) => book.title.indexOf(this.findBook) !== -1));
        });
      },
      minLength: 3,
      select: ( ui: { item: { title: string; }; }) => {
        this.findBook = ui.item.title;
      }
    });
  }
  loadUser(): void {
    const token = localStorage.getItem('token');
    if (token) {
      this.logged = true;
    }
  }

  logOut(): void {
    localStorage.removeItem('token');
    this.logged = false;
    this.route.navigate(['/about']);
  }
  search() {
    this.bookService.getFindBooks(this.findBook).subscribe((data) => {
      this.books = data;
    });
  }
}