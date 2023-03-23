import { Component } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import {HttpClient} from "@angular/common/http";
import {Connector} from "./restapi";

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';

  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService) {}

  ngOnInit(): void {
    //проверяем, существует ли сессия. Если нет - редирект
    if (this.cookieService.get("token") == '' && window.location.pathname != "/login" && window.location.pathname != "/signup") {
      location.replace("/login")
    }
  }
}
