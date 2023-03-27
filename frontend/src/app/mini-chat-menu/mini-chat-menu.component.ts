import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-mini-chat-menu',
  templateUrl: './mini-chat-menu.component.html',
  styleUrls: ['./mini-chat-menu.component.css']
})
export class MiniChatMenuComponent implements OnInit {


  activeChat: boolean = false

  constructor() { }

  ngOnInit(): void {
    if (window.location.pathname == `/chat/${this.chatID}`){
      this.activeChat = true;
    }
  }
  @Input() chatID: number = -1;

}
