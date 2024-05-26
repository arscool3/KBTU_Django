import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomePageComponent } from './home-page/home-page.component';
import { AboutPageComponent } from './about-page/about-page.component';
import { SignInPageComponent } from './sign-in-page/sign-in-page.component';
import { SignUpPageComponent } from './sign-up-page/sign-up-page.component';
import {ProfilePageComponent} from './profile-page/profile-page.component'

import { BookPageComponent } from './book-page/book-page.component';
import { MyBookComponent } from './my-book/my-book.component';
import { InfoBookComponent } from './info-book/info-book.component';
import { CatalogListComponent } from './catalog-list/catalog-list.component';
import { CatalogBooksComponent } from './catalog-books/catalog-books.component';
import {AuthGuard} from "./guards/auth.guard";
import {ManageAccountComponent} from "./manage-account/manage-account.component";
import {PageNotFoundComponent} from "./page-not-found/page-not-found.component";


const routes: Routes = [

  {path: 'home', component: HomePageComponent, canActivate: [AuthGuard],},
  {path: 'about',component: AboutPageComponent},
  {path: 'signin',component: SignInPageComponent},
  {path: 'signup', component: SignUpPageComponent},
  {path: 'profile', component: ProfilePageComponent},
  {path: 'profile/:id', component: ProfilePageComponent},
  {path: 'book', component: BookPageComponent},
  {path: 'profile', component: ProfilePageComponent,canActivate: [AuthGuard],},
  {path: 'mybooks', component: MyBookComponent,canActivate: [AuthGuard],},
  {path: 'book/:id', component: BookPageComponent,canActivate: [AuthGuard],},
  {path: 'catalogs', component: CatalogListComponent,canActivate: [AuthGuard],},
  {path: 'catalogs/:id', component: CatalogBooksComponent,canActivate: [AuthGuard],},
  {path: 'manage-account', component: ManageAccountComponent,canActivate: [AuthGuard],},
  {path: '', redirectTo: 'about', pathMatch: 'full'},
  { path: '**', component: PageNotFoundComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
