import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { EventRoutingModule } from './event-routing/event-routing.module';
import { EventsComponent } from './events/events.component';
import { EventService } from './event/event.service';

@NgModule({
  declarations: [],
  imports: [
    CommonModule,
    EventRoutingModule,
    EventsComponent
  ],
  exports: [
    EventsComponent
  ]
})
export class EventModule { }
