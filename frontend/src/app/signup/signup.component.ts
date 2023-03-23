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
    emptyPassword: false,
    differentPasswords: false,
    incorrectData: false,
  }

  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService) { }

  ngOnInit(): void {
  }

}
