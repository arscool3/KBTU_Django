import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { Doctor, Service } from '../models';
import { ServiceService } from '../service.service';
import { DoctorService } from '../doctor.service';
import { DoctorsComponent } from '../doctors/doctors.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-service',
  standalone: true,
  imports: [DoctorsComponent, CommonModule],
  templateUrl: './service.component.html',
  styleUrl: './service.component.css'
})
export class ServiceComponent implements OnInit {
    service: Service | null = null;
    doctors: Doctor[] | null = null;
  
    constructor(
      private route: ActivatedRoute,
      private router: Router,
      private serviceService: ServiceService,
      private doctorService: DoctorService
    ) { }
  
    ngOnInit(): void {
      this.getServiceDetail();
    }
  
    getServiceDetail(): void {
      const name = this.route.snapshot.paramMap.get('name');
      if (name !== null){
        this.serviceService.getService(name).subscribe(
          (service: Service) => {
            this.service = service;
          },
          (error) => {
            console.error('Failed to fetch service details', error);
          }
        );
      }

      
    }
  
    goBack(): void {
      this.router.navigate(['/services']);
    }

}
