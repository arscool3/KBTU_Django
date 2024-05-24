import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CorzinaComponent } from './corzina.component';

describe('CorzinaComponent', () => {
  let component: CorzinaComponent;
  let fixture: ComponentFixture<CorzinaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CorzinaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CorzinaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
