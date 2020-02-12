import { Injectable } from '@angular/core';
import { Event } from './event';
//import { EVENTS } from './mock-events';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import { MessageService } from './message.service';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class EventService {
  private eventsUrl = 'http://localhost:8000/events/'

  private httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };

  constructor(
    private http: HttpClient,
    private messageService: MessageService
  ) { }

  getEvents(): Observable<Event[]> {
    //this.messageService.add('EventService: the events was fetched');
    //return of(EVENTS);
    return this.http.get<Event[]>(this.eventsUrl)
        .pipe(
            catchError(this.handleError<Event[]>('getEvents',[]))
    );
  }

  getEvent(id: number): Observable<Event> {
    //this.messageService.add(`EventService: fetched event id=${id}`);
    //return of(EVENTS.find(event => event.id === id))
    const url = `${this.eventsUrl}${id}/`;
    return this.http.get<Event>(url).pipe(
        tap(_ => this.log(`fetched event id=${id}`)),
        catchError(this.handleError<Event>(`getEvent id=${id}`))
    );
  }

  updateEvent(event: Event): Observable<any> {
    const url = `${this.eventsUrl}${event.id}/`
    return this.http.put(url, event, this.httpOptions).pipe(
        tap(_ => this.log(`updated event: id=${event.id}`)),
        catchError(this.handleError<any>('updateEvent'))
    );
  }

  addEvent(event: Event): Observable<Event> {
    return this.http.post(this.eventsUrl, event, this.httpOptions).pipe(
        tap((newEvent: Event) => this.log(`add new event: id=${newEvent.id}`)),
        catchError(this.handleError<Event>('addEvent'))
    );
  }

  private log(message: string){
    this.messageService.add(`EventService: ${message}`);
  }

private handleError<T> (operation = 'operation', result?: T) {
  return (error: any): Observable<T> => {

    // TODO: リモート上のロギング基盤にエラーを送信する
    console.error(error); // かわりにconsoleに出力

    // TODO: ユーザーへの開示のためにエラーの変換処理を改善する
    this.log(`${operation} failed: ${error.message}`);

    // 空の結果を返して、アプリを持続可能にする
    return of(result as T);
  };
}
}
