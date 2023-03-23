import {Component, Input, OnInit} from '@angular/core';

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

}
