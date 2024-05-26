import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CatalogBooksComponent } from './catalog-books.component';

describe('CatalogBooksComponent', () => {
  let component: CatalogBooksComponent;
  let fixture: ComponentFixture<CatalogBooksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CatalogBooksComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CatalogBooksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
