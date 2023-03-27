import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MiniChatMenuComponent } from './mini-chat-menu.component';

describe('MiniChatMenuComponent', () => {
  let component: MiniChatMenuComponent;
  let fixture: ComponentFixture<MiniChatMenuComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MiniChatMenuComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MiniChatMenuComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
