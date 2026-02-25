from django.contrib import admin
from .models import Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'organizer', 'date', 'time', 'price', 'seats', 'status')
    list_filter = ('status', 'category', 'date', 'created_at')
    search_fields = ('title', 'description', 'location', 'organizer__username')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'category')
        }),
        ('Event Details', {
            'fields': ('date', 'time', 'location', 'organizer')
        }),
        ('Pricing & Seats', {
            'fields': ('price', 'seats', 'available_seats')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Status', {
            'fields': ('status',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
