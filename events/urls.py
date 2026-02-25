from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('events/', views.event_list, name='event-list'),
    path('events/<int:pk>/', views.event_detail, name='event-detail'),
    path('events/create/', views.create_event, name='create-event'),
    path('events/<int:pk>/edit/', views.edit_event, name='edit-event'),
    path('events/<int:pk>/delete/', views.delete_event, name='delete-event'),
    path('organizer/events/', views.organizer_events, name='organizer-events'),
]
