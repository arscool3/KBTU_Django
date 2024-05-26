import { Component, OnInit } from '@angular/core';
import { Category } from '../models/category';
import { Book } from '../models/book';
import {ActivatedRoute} from "@angular/router";
import { BookService } from '../services/book.service';
import { CategoryService } from '../services/category.service';

@Component({
  selector: 'app-catalog-books',
  templateUrl: './catalog-books.component.html',
  styleUrls: ['./catalog-books.component.css']
})
export class CatalogBooksComponent implements OnInit{
  // category : Category = {
  //   id : 1, 
  //   name: 'Novel'
  // };


  category: Category;
  booklist: Book[];
  loaded: boolean;

  constructor(private route: ActivatedRoute, private bookService: BookService, private categoryService: CategoryService) {
    this.booklist = [] as Book[];
    this.loaded = true;
    this.category = {} as Category;
  }

  ngOnInit(): void {
    this.route.paramMap.subscribe((params) => {
      const category_id = Number(params.get('id'));
      this.loaded = false;
      this.getCategory(category_id);
      this.getBooksByCategory(category_id);
      this.loaded = true;
    })
  }
  getCategory(category_id: number) {
    this.categoryService.getCategory(category_id).subscribe((category) =>{
      this.category = category;
      this.loaded = true;
    },
    // (error) => {
    //   console.log(error);
    //   this.loaded = false;
    //   this.category.error("failed posting");
    // }
    );
  }
  getBooksByCategory(category_id: number) {
    this.bookService.getBooksByCategory(category_id).subscribe((books) => {
      this.booklist = books;
    });
  }
}
