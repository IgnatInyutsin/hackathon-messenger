import {Component, EventEmitter, Input, OnInit, Output} from '@angular/core';

@Component({
  selector: 'app-member-choice',
  templateUrl: './member-choice.component.html',
  styleUrls: ['./member-choice.component.css']
})
export class MemberChoiceComponent implements OnInit {

  constructor() { }

  ngOnInit(): void {
  }
  @Input() username: string = "";
  @Input() activeButton: boolean = false;
  @Output() activeButtonChange = new EventEmitter<boolean>();

  toggleActive() {
    this.activeButton = !this.activeButton;
    this.activeButtonChange.emit(this.activeButton);
  }

}
