import { ComponentFixture, TestBed } from '@angular/core/testing';

import { DoctorVerificationComponent } from './doctor-verification.component';

describe('DoctorVerificationComponent', () => {
  let component: DoctorVerificationComponent;
  let fixture: ComponentFixture<DoctorVerificationComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DoctorVerificationComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(DoctorVerificationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
