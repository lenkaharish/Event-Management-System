from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('conference', 'Conference'),
        ('workshop', 'Workshop'),
        ('seminar', 'Seminar'),
        ('meetup', 'Meetup'),
        ('webinar', 'Webinar'),
        ('other', 'Other'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    ]
    
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    seats = models.IntegerField()
    available_seats = models.IntegerField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def is_upcoming(self):
        from datetime import datetime, time
        event_datetime = timezone.make_aware(
            timezone.datetime.combine(self.date, self.time)
        )
        return event_datetime > timezone.now()
    
    def seats_left(self):
        return self.available_seats
    
    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Events"
