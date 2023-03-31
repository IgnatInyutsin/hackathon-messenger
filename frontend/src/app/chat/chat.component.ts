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
  messageFormText: string = ""
  chatData: any = {
    messages: []
  }
  myID: number;
  ws: WebSocket;
  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService, private activateRoute: ActivatedRoute) { }

  ngAfterViewInit(): void {
    // узнаем историю сообщений
    this.http.get(this.connector.url + "api/chats/" + this.activateRoute.snapshot.params['id'] + "/",
      {headers: new HttpHeaders({"Authorization": "Token " + this.cookieService.get("token")})})
      .subscribe((data) => {
        this.chatData = data;
        console.log(data)
        // подключаем вебсокет
        this.ws = new WebSocket(this.connector.wsUrl + "ws/chat/" + this.activateRoute.snapshot.params['id'] + "/?token=" + this.cookieService.get("token"))
        this.ws.onmessage = (data) => {
          this.getNewMessage(data.data);
          // скролл вниз чата
          setInterval(this.chatBlock.nativeElement.scrollTop = this.chatBlock.nativeElement.scrollHeight, 200);
        }
        // скролл вниз чата
        // скролл вниз чата
        setInterval(this.chatBlock.nativeElement.scrollTop = this.chatBlock.nativeElement.scrollHeight, 200);
      });
    // узнаем свой ID
    this.http.get(this.connector.url + "api/auth/users/me/",
      {headers: new HttpHeaders({"Authorization": "Token " + this.cookieService.get("token")})})
      .subscribe((data: any) => {
        this.myID = data.id;
      })
  }

  getNewMessage(data: any): void {
    data = JSON.parse(data);
    // добавляем сообщение на экран
    this.chatData.messages.push({
      "text": data["text"],
      "author": {
        username: data["author_name"],
        id: data["author_id"]
      }
    });
    this.chatBlock.nativeElement.scroll.top = this.chatBlock.nativeElement.scrollHeight
  }

  sendMessage(): void {
    if (this.messageFormText != "") {
      this.ws.send('{"text": "' + this.messageFormText + '"}')
      this.messageFormText = "";
    }
  }

}
