import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MemberChoiceComponent } from './member-choice.component';

describe('MemberChoiceComponent', () => {
  let component: MemberChoiceComponent;
  let fixture: ComponentFixture<MemberChoiceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MemberChoiceComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MemberChoiceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
