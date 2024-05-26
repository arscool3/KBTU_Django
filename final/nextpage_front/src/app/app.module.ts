import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { TopBarComponent } from './top-bar/top-bar.component';

import { FormsModule } from '@angular/forms';
import { SignUpPageComponent } from './sign-up-page/sign-up-page.component';
import { SignInPageComponent } from './sign-in-page/sign-in-page.component';
import { ReviewComponent } from './review/review.component';

import { HomePageComponent } from './home-page/home-page.component';

import { ReviewPageComponent } from './review-page/review-page.component';
import { ManageAccountComponent } from './manage-account/manage-account.component';
import { AboutPageComponent } from './about-page/about-page.component';
import { FooterComponent } from './footer/footer.component';
import { ProfilePageComponent } from './profile-page/profile-page.component';
// import { CatalogComponent } from './catalog/catalog.component';

import { InfoBookComponent } from './info-book/info-book.component';

import { BookPageComponent } from './book-page/book-page.component';
import { MyBookComponent } from './my-book/my-book.component';
import { CatalogListComponent } from './catalog-list/catalog-list.component';
import { CatalogBooksComponent } from './catalog-books/catalog-books.component';

import {HTTP_INTERCEPTORS, HttpClientModule} from "@angular/common/http";
import {AuthInterceptor} from "./auth.interceptor";
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { UserListComponent } from './user-list/user-list.component';



@NgModule({
  declarations: [
    AppComponent,
    TopBarComponent,
    SignUpPageComponent,
    SignInPageComponent,
    ReviewComponent,

    HomePageComponent,

    AboutPageComponent,
    FooterComponent,
    ProfilePageComponent,

    // CatalogComponent,
    InfoBookComponent,
    ReviewPageComponent,
    ManageAccountComponent,
    MyBookComponent,
    CatalogListComponent,
    CatalogBooksComponent,
    BookPageComponent,
    PageNotFoundComponent,
    UserListComponent,



  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true,
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
