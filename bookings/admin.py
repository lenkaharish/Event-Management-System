from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'user', 'event', 'quantity', 'total_price', 'status', 'payment_status', 'booking_date')
    list_filter = ('status', 'payment_status', 'booking_date', 'event')
    search_fields = ('ticket_number', 'user__username', 'event__title')
    readonly_fields = ('ticket_number', 'created_at', 'updated_at')
    fieldsets = (
        ('Booking Information', {
            'fields': ('ticket_number', 'user', 'event', 'quantity')
        }),
        ('Pricing', {
            'fields': ('total_price',)
        }),
        ('Status', {
            'fields': ('status', 'payment_status')
        }),
        ('Additional Info', {
            'fields': ('notes',)
        }),
        ('Timestamps', {
            'fields': ('booking_date', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
