import { Component, OnInit } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Connector} from "../restapi";
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  // для ngModel
  loginForm: any = {
    username: "",
    password: ""
  }
  // сообщения об ошибках
  errors: any = {
    emptyNickname: false,
    emptyPassword: false,
    incorrectData: false,
  }

  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService) { }

  ngOnInit(): void {}

  login(): void {
    //очищение экрана от любых ошибок
    this.errors.emptyNickname = false;
    this.errors.emptyPassword = false;

    // Валидация
    if (this.loginForm.username == "") {
      this.errors.emptyNickname = true;
      return;
    }
    if (this.loginForm.password == "") {
      this.errors.emptyPassword = true;
      return;
    }

    this.http.post(this.connector.url + "api/auth/token/login/", this.loginForm).
    subscribe((data: any) => {
      // если получилось - добавляем в cookie токен сессии и перезагружаем страницу
      this.cookieService.set("token", data.auth_token)
      location.reload()
    }, (error) => {
      // иначе - сообщение об ошибке
      this.errors.incorrectData = true;
      // очищаем поля
      this.loginForm.password = ""
      this.loginForm.username = ""
    })
  }
}
