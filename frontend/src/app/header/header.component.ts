import {Component, Input, OnInit} from '@angular/core';
import {HttpClient, HttpHeaders} from "@angular/common/http";
import {Connector} from "../restapi";
import {CookieService} from "ngx-cookie-service";
declare var bootstrap: any;

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})

export class HeaderComponent implements OnInit {

  userSearchForm: any = {
    username: "",
    chatName: "",
  }
  errors: any = {
    emptyNickname: false,
    emptyChatName: false,
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
  newDataObj: {[username: string]: [boolean, number]} = {};
  trueIds: Array<number> = [];
  trueIdsObjArr: Array<object> = [];

  myId: number = -1;
  chat: {[chatname: string]: number} = {};
  websockets: any = {};

  notificationUserName: any = ""
  notificationChatName: any = ""
  notificationMessage: any = ""

  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService) { }


  ngOnInit(): void {
    if (window.location.pathname == "/login" || window.location.pathname == "/signup") this.regLogBlockable = true;
    this.http.get(this.connector.url + "api/user/search/", {params: {username: this.userSearchForm.username}, headers:new HttpHeaders({"Authorization": "Token " + this.cookieService.get("token")})}).
    subscribe((data: any) => {
      // здесь уже все перебираем
      this.newData = data.results.map((num: any) => num.username);
      for (const key of this.newData) {
        this.dataObj[key] = false;
      }
      this.newDataObj = data.results.reduce((obj: {[username: string]: [boolean, number]}, {id, username}: {id: number, username: string}) => {
        obj[username] = [false, id];
        return obj;
      }, {});
    }, (error) => {
      // очищаем поля
      this.userSearchForm.username = ""
    })
    this.getMineID()
    this.getMyChats()
  }
  goOut(): void{
    console.log("QQ")
    this.cookieService.delete('token', "/");
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
    this.http.get(this.connector.url + "api/user/search/", {params: {username: this.userSearchForm.username}, headers:new HttpHeaders({"Authorization": "Token " + this.cookieService.get("token")})}).
    subscribe((data: any) => {
      // здесь уже все перебираем
      this.newData = data.results.map((num: any) => num.username);
      for (const key of this.newData) {
        this.dataObj[key] = false;
      }
      this.newDataObj = data.results.reduce((obj: {[username: string]: [boolean, number]}, {id, username}: {id: number, username: string}) => {
        obj[username] = [false, id];
        return obj;
      }, {});
    }, (error) => {
      // очищаем поля
      this.userSearchForm.username = ""
    })
}
  createChat(): void{
    this.errors.emptyChatName = false;
    if (this.userSearchForm.emptyChatName == "") {
      this.errors.emptyChatName = true;
      return;
    }
    for(const key in this.newDataObj){
      let value: any = this.newDataObj[key]
      if (value[0] === true){
        this.trueIds.push(value[1])
      }
    }
    this.getMineID();
    this.trueIdsObjArr = this.trueIds.map(id => ({ id }));
    this.trueIdsObjArr.push({"id": this.myId});
    this.http.post(this.connector.url + "api/chats/", {name:this.userSearchForm.chatName, type:"gm", members: this.trueIdsObjArr}, {headers: new HttpHeaders({"Authorization": "Token " + this.cookieService.get("token")})}).
    subscribe((data: any) => {
      console.log(data);
    }, (error) => {
      // иначе - сообщение об ошибке
      this.userSearchForm.username = "";
      this.userSearchForm.chatName = ""
    })

  }
  getMineID():void{
  this.http.get(this.connector.url + "api/auth/users/me/", {headers:new HttpHeaders({"Authorization": "Token " + this.cookieService.get("token")})}).
  subscribe((data: any) => {
    this.myId= data.id;
    }, (error) => {
  // иначе - сообщение об ошибке
})
  }
  getMyChats(): void{
    this.http.get(this.connector.url + "api/chats/", {headers:new HttpHeaders({"Authorization": "Token " + this.cookieService.get("token")})}).
    subscribe((data: any) => {

      for (const chat of data) {
        this.chat[chat.name] = chat.id;
        this.websockets[chat.name] = new WebSocket(this.connector.wsUrl + "ws/chat/" + chat.id + "/?token=" + this.cookieService.get("token"))
        this.websockets[chat.name].onmessage = (event:any) => {this.createNotification(event.data)}
      }
      console.log(this.chat)

    }, (error) => {
      // иначе - сообщение об ошибке
    })
  }

  createNotification(data: any): void {
    data = JSON.parse(data)
    this.notificationChatName = data["chat_name"]
    this.notificationUserName = data["author_name"]
    this.notificationMessage = data["text"]

    let myAlert = document.querySelector('.toast');
    let bsAlert = new bootstrap.Toast(myAlert);
    bsAlert.show();
  }
}
