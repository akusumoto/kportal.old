import { Component, OnInit } from '@angular/core';
import { EventService } from '../event.service';
import { Event } from '../event';
import { MatTableDataSource } from '@angular/material';

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.css']
})
export class EventsComponent implements OnInit {

  events: Event[];
  displayColumns = ['id', 'date', 'name'];

  constructor(private eventService: EventService) { }

  ngOnInit() {
    this.getService();
  }

  getService() : void {
    this.eventService.getEvents()
      .subscribe(events => this.events = events);
  }

}
