import {Component, Input, OnInit} from '@angular/core';

@Component({
  selector: 'app-message',
  templateUrl: './message.component.html',
  styleUrls: ['./message.component.css']
})
export class MessageComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  @Input() messageId: number = -1;
  @Input() authorId: number = -1;
  @Input() authorName: string = "";
  @Input() textMessage: string = "";

}
