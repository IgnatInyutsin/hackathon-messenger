import {Component, Input, OnInit} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Connector} from "../restapi";
import {CookieService} from "ngx-cookie-service";


@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})

export class HeaderComponent implements OnInit {
  userSearchForm: any = {
    username: "",
  }
  errors: any = {
    emptyNickname: false,
  }
  public showMenu= true;
  name1:string="Egor";
  avatar1:string = "user.png";
  name2:string="Ingnat";
  avatar2:string = "user.png";
  regLogBlockable: boolean = false;
  newData: Array<string> =[];
  dataButtons: Array<boolean> = [];
  test:boolean = false;
  dataObj: { [key: string]: boolean } = {};

  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService) { }

  ngOnInit(): void {
    if (window.location.pathname == "/login" || window.location.pathname == "/signup") this.regLogBlockable = true;
    this.http.get(this.connector.url + "api/user/search/", {params: {username: ""}}).
    subscribe((data: any) => {
      // здесь уже все перебираем
      this.newData = data.results.map((num: any) => num.username);
      for (let i = 0; i<this.newData.length;i++){
        this.dataButtons.push(false);
      };
      for (const key of this.newData) {
        this.dataObj[key] = false;
      }
    }, (error) => {
      // очищаем поля
      this.userSearchForm.username = ""
    })
  }
  goOut(): void{
    this.cookieService.delete('token');
    location.reload()
  }
  userSearch(): void{
    //очищение экрана от любых ошибок
    this.errors.emptyNickname = false;

    // Валидация
    if (this.userSearchForm.username == "") {
      this.errors.emptyNickname = true;
      return;
    }
    this.http.get(this.connector.url + "api/user/search/", {params: {username: this.userSearchForm.username}}).
    subscribe((data: any) => {
      // здесь уже все перебираем
      this.newData = data.results.map((num: any) => num.username);
      for (const key of this.newData) {
        this.dataObj[key] = false;
      }
    }, (error) => {
      // очищаем поля
      this.userSearchForm.username = ""
    })
}
}
