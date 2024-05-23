import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {AuthGuard} from "./core/guards/auth.guard";

const routes: Routes = [
  {
    path: '',
    children: [
      {
        path: '', redirectTo: 'home', pathMatch: 'full'
      },

      {
        path: 'home',
        loadChildren: () =>
          import ('./home/home.module').then(m => m.HomeModule),
        data: {preload: true}
      },
      {
        path: 'auth',
        loadChildren: () =>
          import ('./auth/auth.module').then(m => m.AuthModule),
        data: {preload: true}
      },
    ]
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {
}
