import { Component } from '@angular/core';
import { CookieService } from 'ngx-cookie-service';
import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Connector } from "./restapi";

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
    else if (this.cookieService.get("token") != '') { //проверяем, действителен ли токен
      this.http.get(this.connector.url + "api/auth/users/me/", {
        headers: new HttpHeaders({
          "Authorization": "Token " + this.cookieService.get("token") // добавляем заголовок авторизации
        })
      }).subscribe(() => {
        //если существует - ничего не делаем
      }, () => {
        //если не существует - разлогиниваемся
        this.cookieService.delete("token");
        location.reload();
      });
    }
  }
}
