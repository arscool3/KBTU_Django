import {Component, OnInit} from '@angular/core';
import {OrderService} from "../../services/order.service";
import {Order} from "../../core/models/order";

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.scss']
})
export class OrderComponent implements OnInit {
  orders: Order[] = [];
  selectedOrder: any;
  newOrder: any;

  constructor(private orderService: OrderService) {
  }

  ngOnInit() {
    this.getOrders();
  }

  getOrders(): void {
    this.orderService.getOrders()
      .subscribe(orders => this.orders = orders);
  }

  onSelect(order: Order): void {
    this.selectedOrder = order;
  }

  createOrder(): void {
    this.orderService.createOrder(this.newOrder)
      .subscribe(order => {
        this.orders.push(order);
      });
  }

  updateOrder(): void {
    this.orderService.updateOrder(this.selectedOrder.id, this.selectedOrder)
      .subscribe();
  }

  deleteOrder(): void {
    this.orderService.deleteOrder(this.selectedOrder.id)
      .subscribe(() => {
        this.orders = this.orders.filter(o => o !== this.selectedOrder);
        this.selectedOrder = null;
      });
  }
}
