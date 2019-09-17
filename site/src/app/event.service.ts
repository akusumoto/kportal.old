import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { Event } from './event';

@Injectable({
  providedIn: 'root'
})
export class EventService {
    events: Event[] = [
        {id:1, date:new Date(2019, 0, 1), place:"宮地楽器ホール", station:"武蔵小金井駅", subject:"サンプルイベント１", detail:"これはサンプルイベントです。", owner:"アキラ"},
        {id:2, date:new Date(2019, 1, 1), place:"宮地楽器ホール", station:"武蔵小金井駅", subject:"サンプルイベント２", detail:"これはサンプルイベントです。", owner:"アキラ"},
        {id:3, date:new Date(2019, 9, 1), place:"宮地楽器ホール", station:"武蔵小金井駅", subject:"サンプルイベント３", detail:"これはサンプルイベントです。", owner:"アキラ"},
    ]; 

  events_json_str1 = `[
    {
      "id": 1,
      "date": "2019-11-03T00:00:00.000Z",
      "place": "宮地楽器ホール",
      "station": "武蔵小金井駅",
      "subject": "サンプルイベント１",
      "detail": "これはサンプルイベントです",
      "owner": "アキラ"
    },
    {
      "id": 2,
      "date": "2019-12-03T00:00:00.000Z",
      "place": "宮地楽器ホール",
      "station": "武蔵小金井駅",
      "subject": "サンプルイベント２",
      "detail": "これはサンプルイベントです",
      "owner": "アキラ"
    },
  ]`;

  event_json_str = `[
    {
      "id": 1,
      "date": "2019-11-03T00:00:00.000Z",
      "place": "宮地楽器ホール",
      "station": "武蔵小金井駅",
      "subject": "サンプルイベント",
      "detail": "これはサンプルイベントです",
      "owner": {
        "id": 1,
        "email": "gkusumoto@gmail.com",
        "nickname": "アキラ",
        "status": "active",
        "username": "CB_AKIRA"
      }
    }
  ]`;



  constructor() { }

    getEvents(): Observable<Event[]> {
            //return of(this.events);
        return of(this.events);
    }

    getEvent(id: number): Observable<Event> {
      let event: Event = null;
      for(let ev of this.events){
        if(ev.id == id){
          event = ev;
          break;
        }
      }
      return of(event);
    }

    delete(id: number): void {

    }
}
