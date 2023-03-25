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
import { SignupComponent } from './signup/signup.component';
import { LoginComponent } from './login/login.component';
import { MemberChoiceComponent } from './member-choice/member-choice.component';
import { ChatComponent } from './chat/chat.component';
import { MessageComponent } from './message/message.component';

// определение маршрутов
const appRoutes: Routes = [
  {
    path: "",
    component: HomepageComponent // компонент главной страницы
  },
  {
    path: "signup",
    component: SignupComponent // компонент страницы регистрации
  },
  {
    path: "login",
    component: LoginComponent // компонент страницы входа в аккаунт
  },
  {
    path: "chat",
    component: ChatComponent // компонент страницы чата
  },
];


@NgModule({
  declarations: [
    AppComponent,
    HomepageComponent,
    HeaderComponent,
    FooterComponent,
    ChatMenuComponent,
    SignupComponent,
    LoginComponent,
    MemberChoiceComponent,
    ChatComponent,
    MessageComponent,
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
