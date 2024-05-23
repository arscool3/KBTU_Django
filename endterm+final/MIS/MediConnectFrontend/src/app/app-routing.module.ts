import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { DoctorComponent } from './doctor/doctor.component';
import { DoctorsComponent } from './doctors/doctors.component';
import { ServicesComponent } from './services/services.component';
import { ServiceComponent } from './service/service.component';
import { MyProfileComponent } from './my-profile/my-profile.component';
import { AppointmentComponent } from './appointment/appointment.component';
import { MyAppointmentsComponent } from './my-appointments/my-appointments.component';
import { AppointmentDetailsComponent } from './appointment-details/appointment-details.component';
import { DoctorVerificationComponent } from './doctor-verification/doctor-verification.component'; // Путь может отличаться в зависимости от структуры вашего проекта


const routes: Routes = [
    { path: '', component: HomeComponent },
    { path: 'login', component: LoginComponent },
    { path: 'register', component: RegisterComponent },
    { path: 'doctors', component: DoctorsComponent },
    { path: 'doctors/:id', component: DoctorComponent },
    { path: 'services', component: ServicesComponent },
    { path: 'services/:name', component: ServiceComponent },
    { path: 'my-profile', component: MyProfileComponent },
    { path: 'doctors/:id/appointments', component: AppointmentComponent},
    { path: 'my-appointments',  component: MyAppointmentsComponent },
    { path: 'appointment-details/:id', component: AppointmentDetailsComponent },
    { path: 'verify-license', component: DoctorVerificationComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }


