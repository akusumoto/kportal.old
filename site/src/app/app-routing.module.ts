import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EventsComponent } from './events/events.component';
import { EventDetailComponent } from './event-detail/event-detail.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { EventEditComponent } from './event-edit/event-edit.component';

const routes: Routes = [
  {path: 'event/:id', component: EventDetailComponent},   
  {path: 'event/edit/:id', component: EventEditComponent},   
  {path: 'events', component: EventsComponent},   
  {path: 'dashboard', component: DashboardComponent},
  {path: '', redirectTo: '/dashboard', pathMatch: 'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
