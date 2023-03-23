import { Component, OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Connector} from "../restapi";
import {CookieService} from "ngx-cookie-service";

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent implements OnInit {
  // для ngModel
  signupForm: any = {
    email: "",
    username: "",
    password: "",
    retypePassword:""
  }
  // сообщения об ошибках
  errors: any = {
    emptyNickname: false,
    emptyEmail: false,
    emptyPassword: false,
    differentPasswords: false,
    shortPassword: false,
    incorrectData: false,
  }

  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService) { }

  ngOnInit(): void {
  }
  signup(): void {
    //очищение экрана от любых ошибок
    this.errors.emptyNickname = false;
    this.errors.emptyPassword = false;
    this.errors.differentPasswords = false;
    this.errors.emptyEmail = false;
    this.errors.shortPassword = false;
    // Валидация
    if (this.signupForm.username == "") {
      this.errors.emptyNickname = true;
      return;
    }
    if (this.signupForm.email == "") {
      this.errors.emptyEmail = true;
      return;
    }
    if (this.signupForm.password == "") {
      this.errors.emptyPassword = true;
      return;
    }
    if (this.signupForm.retypePassword != this.signupForm.password) {
      this.errors.differentPasswords = true;
      return;
    }
    if (this.signupForm.password.length < 8) {
      this.errors.shortPassword = true;
      return;
    }

    this.http.post(this.connector.url + "api/auth/users/", this.signupForm).
    subscribe((data: any) => {
      this.http.post(this.connector.url + "api/auth/token/login", this.signupForm).
      subscribe((data: any) => {
        // если получилось - добавляем в cookie токен сессии и перезагружаем страницу
        this.cookieService.set("token", data.auth_token)
        location.reload()
      }, (error) => {
        // иначе - сообщение об ошибке
        this.errors.incorrectData = true;
        // очищаем поля
        this.signupForm.password = ""
        this.signupForm.username = ""
      })
    }, (error) => {
      // иначе - сообщение об ошибке
      this.errors.incorrectData = true;
      // очищаем поля
      this.signupForm.password = ""
      this.signupForm.username = ""
      this.signupForm.email = ""
      this.signupForm.retypePassword = ""
      this.signupForm.shortPassword = ""

    })

  }

}
