import { Component, OnInit } from '@angular/core';
import { UserlistService } from '../services/userlist.service';
import { Review, reviews } from '../models/review';
import { Book, Book2 } from '../models/book';
import { ActivatedRoute } from '@angular/router';
import { BookService } from '../services/book.service';
import { ReviewService } from '../services/review.service';
import { AuthService } from '../services/auth.service';
import { UsersService } from '../services/users.service';
import { ReviewComponent } from '../review/review.component';
import { UserList } from '../models/userlist';
@Component({
  selector: 'app-book-page',
  templateUrl: './book-page.component.html',
  styleUrls: ['./book-page.component.css']
})

export class BookPageComponent implements OnInit{
    option = 'add book'
    b: Book2 ={} as Book2;
    lists: UserList[] = [];
    lists2: UserList[] = [];
    userlist: UserList = {} as UserList;
    rate : number = 0;
    rating: number = 0;
    selectedOption: string | undefined;
    add = false;
    name: string | undefined = "Nurkhan";
    review: string | undefined;
    id: number = 0;
    books : Book[] = []
    book : Book
    userId : number = 0
    reviews: Review[] = []
    selectElement = document.getElementById('select') as HTMLSelectElement;
    constructor(private route: ActivatedRoute, private bookService: BookService, private reviewService: ReviewService,private userService: UsersService, private userListService: UserlistService){
      //   this.myButton = document.getElementById('show')!;
      //   this.myButton.onclick = this.handleClick.bind(this);
      this.book = {} as Book;

    }
    ngOnInit(): void{
      const ratingItemsList = document.querySelectorAll('.rating_item');
      const ratingItemsArray = Array.prototype.slice.call(ratingItemsList);
      ratingItemsArray.forEach(item => item.parentNode.dataset.totalValue = this.rate)
      this.userService.logged().subscribe((user) => this.userId = user.id)
      this.selectedOption = 'Reading';
      this.route.paramMap.subscribe((params) => {
        this.id = Number(params.get('id'));
        this.getCurrentRating();
        this.getReviews(this.id);
        this.b.book = this.id;
        this.getUsersLists();
        this.getListOfBook();
      })
      // this.getListOfBook();
      
      
      
    }
    getUsersLists() {
      this.userListService.getUsersLists().subscribe((userList) =>{
        this.lists = userList;
      })
    }
    getReviews(id: number){
      this.reviewService.getReviews(id).subscribe((review) => this.reviews = review);
    }
    getCurrentRating(){
        this.reviewService.getRating(this.id).subscribe((rating) => {this.rating = Math.round(rating.sum / rating.count * 100) / 100 * 20; this.Star(this.rating)});
    }
    updateRating(){
      this.reviewService.getRating(this.id).subscribe((rating) => {this.rating = Math.round((rating.sum + this.rate) / (rating.count + 1) * 100) / 100 * 100 / 5; this.Star(this.rating)});
      if (this.rating == 0){
        this.rating = this.rate * 20;
        this.Star(this.rating);
      }
      
    }
    getBook(id:number){
      this.bookService.getBookById(id).subscribe((book) => {this.book = book;
      console.log(this.book.title)});
    }
    Star(rating: number){
      const myStar = document.getElementById('rating_item_part');
      myStar!.style.background = `linear-gradient(to right,yellow ${rating}%, transparent 10%)`;
      myStar!.style.webkitBackgroundClip = 'text';
      myStar!.style.webkitTextFillColor = 'transparent';
    }
    changeRate(rate:number){
        this.rate = rate;
        const ratingItemsList = document.querySelectorAll('.rating_item');
        const ratingItemsArray = Array.prototype.slice.call(ratingItemsList);
        ratingItemsArray.forEach(item => item.parentNode.dataset.totalValue = this.rate)
    }
    saveOption(){
      this.selectElement = document.getElementById('select') as HTMLSelectElement;
      this.selectedOption = this.selectElement.value;
      // this.selectedOption = this.userListService.
     
      for (let i = 0; i < this.lists.length; i++) {
        if (this.lists[i].name != this.selectedOption) {
          this.userListService.deletetBookFromList(this.lists[i].name, this.b).subscribe((userlist) => {
            this.lists[i] = userlist;
          });
        }
      }
   
      // if (this.lists.length > 0) {
      //   // this.selectedOption = this.lists[0].name;
      //   this.userListService.deletetBookFromList(this.lists[0].name, this.b).subscribe((userlist) => {
      //     this.lists[0] = userlist;
      //   });
      // }
      
      if (this.selectedOption != 'AddBook' && this.selectedOption != 'Delete') {
        this.userListService.postBookToList(this.selectedOption, this.b).subscribe((userlist) => {
          this.userlist = userlist;
        });
      }
    }

    onSubmit() {
      this.userService.logged().subscribe((user) => {this.reviewService.postReview(this.review!,this.rate,this.id,user.id);this.reviews.push({
        id: user.id,
        user: user,
        user_name: user.username,
        rating: this.rate,
        review: this.review!,
        book: this.book});
        this.updateRating();
        })
      // reviews.push(
      //   {id:this.id,
      //    username:this.name!,
      //    rating: this.rate,
      //    review: this.review!,
      //    book: this.id}
      //   );
      // console.log(reviews)
      // console.log('Name:', this.name);
      // console.log('Rating:', this.rate);
      // console.log('Review:', this.review);
    }

    getListOfBook(){
      this.userListService.getListOfBook(this.id).subscribe((list) => {this.lists2 = list;
        if (this.lists2.length > 0){
        for(let list1 of list){
          if(Number(list1.user) == this.userId){
              this.option = list1.name
          }
        }
        // this.option = this.lists2[0].name;
      };
      }
      );
    }
}
