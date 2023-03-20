import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})

export class HeaderComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {

  }
  public showMenu= true;
  name1:string="Egor";
  avatar1:string = "user.png";
  name2:string="Ingnar";
  avatar2:string = "user.png";
}
