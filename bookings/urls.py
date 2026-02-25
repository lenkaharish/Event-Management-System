from django.urls import path
from . import views

urlpatterns = [
    path('book/<int:event_id>/', views.create_booking, name='create-booking'),
    path('booking/<int:pk>/', views.booking_detail, name='booking-detail'),
    path('my-bookings/', views.user_bookings, name='user-bookings'),
    path('booking/<int:pk>/cancel/', views.cancel_booking, name='cancel-booking'),
    path('booking/<int:pk>/download-ticket/', views.download_ticket, name='download-ticket'),
]
