import {Component, OnInit} from '@angular/core';
import {Product} from "../../core/models/Product";
import {ActivatedRoute, Router} from "@angular/router";
import {ProductService} from "../../services/product.service";

@Component({
  selector: 'app-corzina',
  templateUrl: './corzina.component.html',
  styleUrls: ['./corzina.component.scss']
})
export class CorzinaComponent implements OnInit {
  products?: Product[];
  // currentTutorial: Tutorial = {};
  currentIndex = -1;
  title = '';
  company: string = '';

  constructor(private activRoute: ActivatedRoute, private prodService: ProductService, private router: Router) {
  }

  ngOnInit(): void {
    this.products = this.prodService.corPruducts
  }


  deleteProduct(i: number) {
    this.products?.splice(i, 1);
  }

  oform(i: number) {
    window.alert("Заказ оформлен, ожидайте доставки")
    this.products?.splice(i, 1);
  }
}
