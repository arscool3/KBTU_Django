import { Component } from '@angular/core';
import { Book, books } from '../models/book';
import { ActivatedRoute } from '@angular/router';
import { BookService } from '../services/book.service';
import { UserlistService } from '../services/userlist.service';
@Component({
  selector: 'app-info-book',
  templateUrl: './info-book.component.html',
  styleUrls: ['./info-book.component.css']
})
export class InfoBookComponent {
    check = false;
    id : number | undefined;
    fullDes: string = ''
    book : Book;
    home = false;
    appear = false;
    constructor(private route: ActivatedRoute, private bookService: BookService, private userList: UserlistService){
       this.book = {} as Book
    }

    ngOnInit(): void{
      this.route.paramMap.subscribe((params) => {
        const id = Number(params.get('id'));
        if (id != 0){
          this.getBook(id);
        }
        if (id == 0){
          // this.home = true;
          this.userList.getBooksOfList('Reading').subscribe((books) => {
            if(books != undefined && books.length != 0){
                this.book = books[0];
                this.getInfo(this.book.description);
                this.changeDes();
            }
          })
        }
        console.log(this.book);
      })
    }
    getBook(id:number){
      this.bookService.getBookById(id).subscribe((book) => {this.book = book;
      this.getInfo(this.book.description);});
    }
    getHome(){
      
    }
    getInfo(description:string): void{
      this.fullDes = description;
      if (description.length >= 328){
        this.appear = true;
        this.check = true;
        this.changeDes();
        // this.check = true;
      }
    }
    checkSize(){
        if (this.book.description.length < 328){
            this.appear = false;
        }
        else{
          this.appear = true;
        }
    }
    changeDes(){
      if (this.check == true){
        this.book.description = this.fullDes
      }
      else{
        this.book.description = this.fullDes.substring(0,328)
        let words = this.book.description.split(' ');
        words.pop()
        this.book.description = words.join(" ");
      }
      this.check = !this.check
    }
}
