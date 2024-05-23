import {Component, OnInit} from '@angular/core';
import {Category} from "../../core/models/Category";
import {ActivatedRoute, Router} from "@angular/router";
import {CategoryService} from "../../services/category.service";
import {Product} from "../../core/models/Product";
import {ProductService} from "../../services/product.service";

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.scss']
})
export class ProductsComponent implements OnInit {
  products?: Product[];
  // currentTutorial: Tutorial = {};
  currentIndex = -1;
  title = '';
  company: string = '';

  constructor(private activRoute: ActivatedRoute, private prodService: ProductService, private router: Router) {
  }

  ngOnInit(): void {
    this.getProducts();
  }

  getProducts(): void {
    this.prodService.getAll()
      .subscribe(
        (data: Product[] | undefined) => {
          this.products = data;
          console.log(data);
        },
        (error: any) => {
          console.log(error);
        });
  }


  goToProduct(id: number) {
    this.router.navigate([`products/${id}`])

  }
}
