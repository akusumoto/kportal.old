import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Event } from './event';

@Injectable({
  providedIn: 'root'
})
export class EventService {
    events: Event[] = [
        {id:1, name:'Event1', date:new Date(2019, 1, 1)},
        {id:2, name:'Event2', date:new Date(2019, 2, 1)},
        {id:3, name:'Event3', date:new Date(2019, 10, 1)},
    ]; 

  constructor() { }

    getEvents(): Observable<Event[]> {
        return of(this.events);
    }

    getEvent(id: number): Observable<Event> {
      let selectedEvent: Event = null;
      for(let event of this.events){
        if(event.id == id){
          selectedEvent = event;
          break;
        }
      }
      return of(selectedEvent);
    }

    delete(id: number): void {

    }
}
