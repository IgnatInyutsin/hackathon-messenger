import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {FormsModule} from "@angular/forms";
import {Routes, RouterModule} from '@angular/router';

import { AppComponent } from './app.component';
import { PreloaderComponent } from './preloader/preloader.component';
import { HttpClientModule }   from '@angular/common/http';
import {CookieService} from "ngx-cookie-service";
import { HomepageComponent } from './homepage/homepage.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { LoginComponent } from './login/login.component';
import { RegistrationComponent } from './registration/registration.component';
import {Connector} from "./restapi";
// определение маршрутов
const appRoutes: Routes = [
  {
    path: "",
    component: HomepageComponent // компонент главной страницы
  },
  {
    path: "registration",
    component: RegistrationComponent, // Компонент модуля, который редиректит на первое задание модуля
  },
  {
    path: "login",
    component: LoginComponent, // Компонент модуля, который редиректит на первое задание модуля
  },
];


@NgModule({
  declarations: [
    AppComponent,
    PreloaderComponent,
    HomepageComponent,
    HeaderComponent,
    FooterComponent,
    LoginComponent,
    RegistrationComponent,
  ],
  imports: [
    BrowserModule,
    FormsModule,
    RouterModule.forRoot(appRoutes),
    HttpClientModule,
  ],
  providers: [
    CookieService,
    Connector
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
