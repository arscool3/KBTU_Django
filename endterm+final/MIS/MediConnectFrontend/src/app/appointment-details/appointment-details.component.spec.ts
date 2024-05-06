import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AppointmentDetailsComponent } from './appointment-details.component';

describe('AppointmentDetailsComponent', () => {
  let component: AppointmentDetailsComponent;
  let fixture: ComponentFixture<AppointmentDetailsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AppointmentDetailsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AppointmentDetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
