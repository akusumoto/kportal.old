import { Injectable } from '@angular/core';
import { Event } from './event';
import { EVENTS } from './mock-events';
import { Observable, of } from 'rxjs';
import { MessageService } from './message.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class EventService {
  private eventsUrl = 'http://localhost:8000/events/'

  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }

  getEvents(): Observable<Event[]> {
    //this.messageService.add('EventService: the events was fetched');
    //return of(EVENTS);
    return this.http.get<Event[]>(this.eventsUrl);
  }

  getEvent(id: number): Observable<Event> {
    this.messageService.add(`EventService: fetched event id=${id}`);
    return of(EVENTS.find(event => event.id === id))
  }

  private log(message: string){
    this.messageService.add(`EventService: ${message}`);
  }
}
