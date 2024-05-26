import { Component, OnInit } from '@angular/core';
import { Category } from '../models/category';
import { CategoryService } from '../services/category.service';


@Component({
  selector: 'app-catalog-list',
  templateUrl: './catalog-list.component.html',
  styleUrls: ['./catalog-list.component.css']
})
export class CatalogListComponent implements OnInit{
  categoryList: Category[];
  loaded: boolean;

  constructor(private categoryService: CategoryService) {
    this.categoryList = []
    this.loaded = true;
  }

  ngOnInit(): void {
    this.getCategories();
  }

  getCategories() {
    this.loaded = false;
    this.categoryService.getCategories().subscribe((categories) =>{
      this.categoryList = categories;
      this.loaded = true;
    })
  }


  
}
