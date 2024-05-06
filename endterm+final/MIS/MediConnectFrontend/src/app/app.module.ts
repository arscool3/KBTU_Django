import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';
import { LoginComponent } from './login/login.component'; 
import { RegisterComponent } from './register/register.component';
import { ProfileService } from './profile.service';
import { AuthService } from './auth.service';
import { CommonModule } from '@angular/common';
import { MyProfileComponent } from './my-profile/my-profile.component';
import { HomeComponent } from './home/home.component';
import { DoctorComponent } from './doctor/doctor.component';
import { AppointmentComponent } from './appointment/appointment.component';
import { ServiceComponent } from './service/service.component';
import { DoctorsComponent } from './doctors/doctors.component';
import { MyAppointmentsComponent } from './my-appointments/my-appointments.component';
import { AppointmentDetailsComponent } from './appointment-details/appointment-details.component';
import { DoctorVerificationComponent } from './doctor-verification/doctor-verification.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    MyProfileComponent,
    HomeComponent,
    DoctorComponent,
    AppointmentComponent,
    MyAppointmentsComponent,
    AppointmentDetailsComponent,
    DoctorVerificationComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule,
    RouterModule,
    ReactiveFormsModule,
    CommonModule,
    DoctorsComponent
  ],
  providers: [ProfileService, AuthService],
  bootstrap: [AppComponent]
})
export class AppModule { }


