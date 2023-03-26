import { Component, AfterViewInit, ViewChild } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Connector} from "../restapi";
import { CookieService } from 'ngx-cookie-service';
import { ActivatedRoute} from '@angular/router';

@Component({
  selector: 'app-chat',
  templateUrl: './chat.component.html',
  styleUrls: ['./chat.component.css']
})
export class ChatComponent implements AfterViewInit {
  @ViewChild('chatblock', {static: false}) chatBlock:any;
  chatData: any = {
    messages: []
  }
  myID: number;

  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService, private activateRoute: ActivatedRoute) { }

  ngAfterViewInit(): void {
    // скролл вниз чата
    this.chatBlock.nativeElement.scrollTop = this.chatBlock.nativeElement.scrollHeight;
    // узнаем историю сообщений
    this.http.get(this.connector.url + "api/chats/" + this.activateRoute.snapshot.params['id'] + "/",
      {headers: new HttpHeaders({"Authorization": "Token " + this.cookieService.get("token")})})
      .subscribe((data) => {
        this.chatData = data;
        console.log(data)
      });
    // узнаем свой ID
    this.http.get(this.connector.url + "api/auth/users/me/",
      {headers: new HttpHeaders({"Authorization": "Token " + this.cookieService.get("token")})})
      .subscribe((data: any) => {
        this.myID = data.id;
      })
  }
}
