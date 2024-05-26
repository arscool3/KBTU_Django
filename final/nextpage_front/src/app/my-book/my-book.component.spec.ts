import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MyBookComponent } from './my-book.component';

describe('MyBookComponent', () => {
  let component: MyBookComponent;
  let fixture: ComponentFixture<MyBookComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MyBookComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(MyBookComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
