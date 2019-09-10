import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Event } from './event';

@Injectable({
  providedIn: 'root'
})
export class EventService {

    events: Event[] = [
        {id:1, name:'Event1', date:null},
        {id:2, name:'Event2', date:null},
        {id:3, name:'Event3', date:null},
    ]; 

  constructor() { }

    getEvents(): Observable<Event[]> {
        return of(this.events);
    }
}
