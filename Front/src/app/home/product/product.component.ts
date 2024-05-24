import {Component, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {ProductService} from "../../services/product.service";
import {ActivatedRoute, Router} from "@angular/router";
import {Product} from "../../core/models/Product";

@Component({
  selector: 'app-product',
  templateUrl: './product.component.html',
  styleUrls: ['./product.component.scss']
})
export class ProductComponent implements OnInit {
  ID: number = 0;
  curProduct: { small_descr: string; price: number; name: string; description: string; photo: string } = {
    name: '',
    small_descr: '',
    description: '',
    photo: '',
    price: 0,

  };

  constructor(private hhtp: HttpClient, private productService: ProductService, private activRoute: ActivatedRoute, private router: Router) {
  }

  ngOnInit(): void {
    this.ID = Number(this.activRoute.snapshot.params['id'])
    this.getProduct(this.ID)

  }

  getProduct(id: number): void {
    this.productService.get(id)
      .subscribe(
        data => {
          this.curProduct = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  addCorzina(product: { small_descr: string; price: number; name: string; description: string; photo: string }) {
    this.productService.addToCorzina(product);
  }
}
