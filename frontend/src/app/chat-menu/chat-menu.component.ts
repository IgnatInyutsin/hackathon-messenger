import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-chat-menu',
  templateUrl: './chat-menu.component.html',
  styleUrls: ['./chat-menu.component.css']
})
export class ChatMenuComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  @Input() chatName: string = "";
  // @Input() lastChatMessage: string = "";
  @Input() chatID: number = -1;
}
