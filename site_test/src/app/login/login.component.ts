import { Component, OnInit } from '@angular/core';

import { LoginService } from '../login.service';
import { MessageService } from '../message.service';
import { User } from '../user';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent implements OnInit {

  constructor(private loginService: LoginService,
              private messageService: MessageService) { }

  ngOnInit(): void {
  }

  login(username: string, password: string) {
    return this.loginService.login({username: username, email: 'aa@xample.com', password: password} as User)
            .subscribe(token => {this.messageService.add(`${token}`);});
  }
}
