import { Component, OnInit } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {Connector} from "../restapi";
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-homepage',
  templateUrl: './homepage.component.html',
  styleUrls: ['./homepage.component.css']
})
export class HomepageComponent implements OnInit {
  constructor(private http: HttpClient, private connector: Connector, public cookieService: CookieService) {
  }

  ngOnInit(): void {}
}
