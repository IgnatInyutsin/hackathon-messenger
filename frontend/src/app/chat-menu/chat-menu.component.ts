import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-chat-menu',
  templateUrl: './chat-menu.component.html',
  styleUrls: ['./chat-menu.component.css']
})
export class ChatMenuComponent implements OnInit {

  activeChat: boolean = false

  constructor() { }

  ngOnInit(): void {
    if (window.location.pathname == `/chat/${this.chatID}`){
      this.activeChat = true;
    }
  }
  @Input() chatName: string = "";
  // @Input() lastChatMessage: string = "";
  @Input() chatID: number = -1;
}
