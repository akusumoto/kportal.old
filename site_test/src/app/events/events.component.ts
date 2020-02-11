import { Component, OnInit } from '@angular/core';
import { Event } from '../event';
import { EventService } from '../event.service';
import { MessageService } from '../message.service';

@Component({
  selector: 'app-events',
  templateUrl: './events.component.html',
  styleUrls: ['./events.component.scss']
})
export class EventsComponent implements OnInit {
  events: Event[];
  selectedEvent: Event;

  constructor(private eventService: EventService,
              private messageService: MessageService) { }

  ngOnInit(): void {
    this.getEvents();
  }

/*
  onSelect(event: Event): void {
    this.selectedEvent = event;
    this.messageService.add(`EventService: selected event id=${event.id}`);
  }
*/

  getEvents(): void {
    //this.events = this.eventService.getEvents();
    this.eventService.getEvents()
        .subscribe(events => this.events = events);
  }

}
