from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from events.models import Event
from .models import Booking
from .forms import BookingForm

@login_required(login_url='login')
def create_booking(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    
    if event.available_seats <= 0:
        messages.error(request, 'This event is fully booked.')
        return redirect('event-detail', pk=event_id)
    
    if request.method == 'POST':
        form = BookingForm(request.POST, event=event)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.event = event
            
            # Check if enough seats available
            if booking.quantity > event.available_seats:
                messages.error(request, f'Only {event.available_seats} seats available.')
                return redirect('event-detail', pk=event_id)
            
            booking.total_price = event.price * booking.quantity
            booking.save()
            
            # Update event available seats
            event.available_seats -= booking.quantity
            event.save()
            
            messages.success(request, 'Booking confirmed! Check your booking details.')
            return redirect('booking-detail', pk=booking.pk)
    else:
        form = BookingForm(event=event)
    
    context = {
        'form': form,
        'event': event,
    }
    return render(request, 'bookings/booking_form.html', context)

@login_required(login_url='login')
def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    
    if booking.user != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to view this booking.')
        return redirect('home')
    
    context = {'booking': booking}
    return render(request, 'bookings/booking_detail.html', context)

@login_required(login_url='login')
def user_bookings(request):
    bookings = request.user.bookings.all().order_by('-booking_date')
    context = {'bookings': bookings}
    return render(request, 'bookings/user_bookings.html', context)

@login_required(login_url='login')
def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    
    if booking.user != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to cancel this booking.')
        return redirect('home')
    
    if booking.status == 'cancelled':
        messages.error(request, 'This booking is already cancelled.')
        return redirect('booking-detail', pk=booking.pk)
    
    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        
        # Restore event seats
        booking.event.available_seats += booking.quantity
        booking.event.save()
        
        messages.success(request, 'Booking cancelled successfully.')
        return redirect('user-bookings')
    
    context = {'booking': booking}
    return render(request, 'bookings/cancel_booking.html', context)

@login_required(login_url='login')
def download_ticket(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    
    if booking.user != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to download this ticket.')
        return redirect('home')
    
    
    
    # Create a simple ticket as HTML (can be enhanced to PDF)
    response = HttpResponse(content_type='text/html')
    response['Content-Disposition'] = f'attachment; filename="ticket_{booking.ticket_number}.html"'
    
    html_content = f"""
    <html>
    <head>
        <title>Event Ticket</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            .ticket {{ border: 2px solid #333; padding: 20px; max-width: 600px; margin: 0 auto; }}
            .header {{ text-align: center; margin-bottom: 20px; }}
            .details {{ margin: 15px 0; }}
            .label {{ font-weight: bold; }}
        </style>
    </head>
    <body>
        <div class="ticket">
            <div class="header">
                <h1>EVENT TICKET</h1>
                <p>Ticket Number: {booking.ticket_number}</p>
            </div>
            <div class="details">
                <div><span class="label">Event:</span> {booking.event.title}</div>
                <div><span class="label">Attendee:</span> {booking.user.get_full_name() or booking.user.username}</div>
                <div><span class="label">Date:</span> {booking.event.date}</div>
                <div><span class="label">Time:</span> {booking.event.time}</div>
                <div><span class="label">Location:</span> {booking.event.location}</div>
                <div><span class="label">Number of Tickets:</span> {booking.quantity}</div>
                <div><span class="label">Total Price:</span> ₹{booking.total_price}</div>
                <div><span class="label">Status:</span> {booking.get_status_display()}</div>
                <div><span class="label">Booking Date:</span> {booking.booking_date}</div>
            </div>
        </div>
    </body>
    </html>
    """
    
    response.write(html_content)
    return response
