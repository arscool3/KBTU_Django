import { TestBed } from '@angular/core/testing';

import { OrderProductService } from './order-product.service';

describe('OrderProductService', () => {
  let service: OrderProductService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(OrderProductService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
