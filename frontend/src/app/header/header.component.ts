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
  public showMenu= true;
  name1:string="Egor";
  avatar1:string = "user.png";
  name2:string="Ingnat";
  avatar2:string = "user.png";
  regLogBlockable: boolean = false;
  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService) { }

  ngOnInit(): void {
    if (window.location.pathname == "/login" || window.location.pathname == "/signup") this.regLogBlockable = true;
  }
  goOut(): void{
    this.cookieService.delete('token');
    location.reload()
  }
}
