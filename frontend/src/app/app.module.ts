import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {FormsModule} from "@angular/forms";
import {Routes, RouterModule} from '@angular/router';

import { AppComponent } from './app.component';
import { HttpClientModule }   from '@angular/common/http';
import {CookieService} from "ngx-cookie-service";
import { HomepageComponent } from './homepage/homepage.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import {Connector} from "./restapi";
import { ChatMenuComponent } from './chat-menu/chat-menu.component';

// определение маршрутов
const appRoutes: Routes = [
  {
    path: "",
    component: HomepageComponent // компонент главной страницы
  },
];


@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
    HeaderComponent,
    FooterComponent,
    ChatMenuComponent,
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
