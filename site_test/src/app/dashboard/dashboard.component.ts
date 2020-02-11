import { Component, OnInit } from '@angular/core';
import { EventService } from '../event.service';
import { Event } from '../event';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.scss']
})
export class DashboardComponent implements OnInit {
  events: Event[] = [];

  constructor(private eventService: EventService) { }

  ngOnInit(): void {
    this.getEvents();
  }

  getEvents(): void {
    this.eventService.getEvents()
        .subscribe(events => this.events = events.slice(1,3)); 
  }
}
