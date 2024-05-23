import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {Category} from "../core/models/Category";
import {Product} from "../core/models/Product";

@Injectable({
  providedIn: 'root'
})
export class ProductService {
  private baseUrl: string = 'http://localhost:8000/api/products';
  public corPruducts: Product[] = []

  constructor(private http: HttpClient) {
  }

  addToCorzina(product: { small_descr: string; price: number; name: string; description: string; photo: string }) {
    this.corPruducts.push(<Product>product);
  }

  getAll(): Observable<Product[]> {
    return this.http.get<Product[]>(this.baseUrl);
  }

  get(id: number): Observable<Product> {
    return this.http.get<Product>(`${(this.baseUrl)}/${id}`);
  }

  create(data: any): Observable<any> {
    return this.http.post(this.baseUrl, data);
  }
}
