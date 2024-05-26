import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InfoBookComponent } from './info-book.component';

describe('InfoBookComponent', () => {
  let component: InfoBookComponent;
  let fixture: ComponentFixture<InfoBookComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InfoBookComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InfoBookComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
