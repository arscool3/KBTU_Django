import {Component, OnInit} from '@angular/core';
import {Category} from "../../core/models/Category";
import {ActivatedRoute, Router} from "@angular/router";
import {CategoryService} from "../../services/category.service";

@Component({
  selector: 'app-categories',
  templateUrl: './categories.component.html',
  styleUrls: ['./categories.component.scss']
})
export class CategoriesComponent implements OnInit {
  categories?: Category[];
  // currentTutorial: Tutorial = {};
  currentIndex = -1;
  title = '';
  company: string = '';

  constructor(private activRoute: ActivatedRoute, private categoryService: CategoryService, private router: Router) {
  }

  ngOnInit(): void {
    this.getCompanies();
  }

  getCompanies(): void {
    this.categoryService.getAll()
      .subscribe(
        (data: Category[] | undefined) => {
          this.categories = data;
          console.log(data);
        },
        (error: any) => {
          console.log(error);
        });
  }
  goToCategory(i: number) {
    this.router.navigate([`categories/${i}`])
  }
}
