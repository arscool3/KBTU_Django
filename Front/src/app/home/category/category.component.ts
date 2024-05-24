import {Component, OnInit} from '@angular/core';
import {Category} from "../../core/models/Category";
import {HttpClient} from "@angular/common/http";
import {CategoryService} from "../../services/category.service";
import {ActivatedRoute, Router} from "@angular/router";
import {Observable} from "rxjs";
import {Product} from "../../core/models/Product";

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.scss']
})
export class CategoryComponent implements OnInit{
  catID: number;
  catUrl: string = 'http://localhost:8000/api/categories/';
  curCategory: { name: string; photo: string; } = {
    name: '',
    photo: ''
  };
  public products: Product[] = [];

  constructor(private router: Router, private hhtp: HttpClient, private categoryService: CategoryService, private activRoute: ActivatedRoute) {
    this.catID = 0;
  }

  ngOnInit(): void {
    this.catID = Number(this.activRoute.snapshot.params['id']) + 1
    this.getCategory(this.catID)
    this.catUrl = this.catUrl + this.catID + '/products'
    this.getProducts()
    console.log(this.catUrl)

  }

  getCategory(id: number): void {
    this.categoryService.get(id)
      .subscribe(
        data => {
          this.curCategory = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  getProducts(): void {
    this.getAllByCategory()
      .subscribe(
        (data: Product[]) => {
          this.products = data;
          console.log(data);
        },
        (error: any) => {
          console.log(error);
        });
  }

  getAllByCategory(): Observable<Product[]> {
    return this.hhtp.get<Product[]>(this.catUrl);
  }

  goToProduct(id: number) {
    this.router.navigate([`/products/${id}`])
  }
}
