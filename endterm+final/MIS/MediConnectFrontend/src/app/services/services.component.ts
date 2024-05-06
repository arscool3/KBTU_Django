import { Component } from '@angular/core';
import { Service } from '../models';
import { ServiceService } from '../service.service';
import { Router } from '@angular/router';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-services',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './services.component.html',
  styleUrl: './services.component.css'
})
export class ServicesComponent {
  services: Service[] = [];
  constructor(private serviceService: ServiceService, private router: Router) {}

  ngOnInit(): void {
    this.serviceService.getServices().subscribe(
      (services: Service[]) => {
        this.services = services;
      },
      (error) => {
        console.error('Failed to fetch services', error);
      }
    );
  }

  viewServiceDetails(service: Service): void {
    this.router.navigate(['/services', service.name]);
  }

  goHome(): void {
    this.router.navigate(['/']);
  }
}

