import {Component, Input} from '@angular/core';
import {Review} from "../models/review";
import { reviews } from '../models/review';
import { ActivatedRoute } from '@angular/router';
import { ReviewService } from '../services/review.service';
@Component({
  selector: 'app-review',
  templateUrl: './review.component.html',
  styleUrls: ['./review.component.css']
})
export class ReviewComponent {
  // reviews: Review[]
  profile: string | undefined;
  rating: number | undefined;
  @Input() reviews: Review[] = [];
  // static reviews: any;
  constructor(private route: ActivatedRoute, private reviewService: ReviewService){
    this.reviews = [] as Review[]
 }
  mylist = reviews;
  ngOnInit(): void{
    this.route.paramMap.subscribe((params) => {
      const id = Number(params.get('id'));
      // this.getReviews(id);
    })
    // this.myList = reviews.filter((book) => book.bookId == this.bookId);
    // alert(this.selectedOption)
    // const selectElement = document.getElementById('select') as HTMLSelectElement;
    // this.selectedOption = selectElement.value;
  }
  // getReviews(id: number){
    // this.reviewService.getReviews(id).subscribe((review) => this.reviews = review);
  // }
}
