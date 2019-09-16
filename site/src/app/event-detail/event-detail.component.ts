import { Component, OnInit, Input } from '@angular/core';
import { Event } from '../event';
import { EventService } from '../event.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-event-detail',
  templateUrl: './event-detail.component.html',
  styleUrls: ['./event-detail.component.css']
})
export class EventDetailComponent implements OnInit {

  @Input() event: Event;
  id: number;

  constructor(private eventService: EventService,
              private route: ActivatedRoute) { }

  ngOnInit() {
    this.id = parseInt(this.route.snapshot.paramMap.get("id"));
    this.getService();
  }

  getService(): void {
    this.eventService.getEvent(this.id).subscribe(event => this.event = event);
  }

  delete(id: number){
    this.eventService.delete(id);
  }
}
