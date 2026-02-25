from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm, EventSearchForm
from accounts.models import UserProfile
from bookings.models import Booking

def home(request):
    featured_events = Event.objects.filter(status='approved').order_by('-created_at')[:6]
    recent_events = Event.objects.filter(status='approved').order_by('-date')[:3]
    context = {
        'featured_events': featured_events,
        'recent_events': recent_events,
        'total_events': Event.objects.filter(status='approved').count(),
        'total_users': UserProfile.objects.count(),
    }
    return render(request, 'events/home.html', context)

def event_list(request):
    events = Event.objects.filter(status='approved')
    form = EventSearchForm(request.GET or None)
    
    if form.is_valid():
        search = form.cleaned_data.get('search')
        category = form.cleaned_data.get('category')
        date_from = form.cleaned_data.get('date_from')
        price_max = form.cleaned_data.get('price_max')
        
        if search:
            events = events.filter(Q(title__icontains=search) | Q(description__icontains=search))
        
        if category:
            events = events.filter(category=category)
        
        if date_from:
            events = events.filter(date__gte=date_from)
        
        if price_max is not None:
            events = events.filter(price__lte=price_max)
    
    context = {
        'events': events,
        'form': form,
    }
    return render(request, 'events/event_list.html', context)

def event_detail(request, pk):
    event = get_object_or_404(Event, pk=pk)
    organizer_profile = UserProfile.objects.get_or_create(user=event.organizer)[0]
    user_booking = None
    
    if request.user.is_authenticated:
        user_booking = Booking.objects.filter(user=request.user, event=event).first()
    
    context = {
        'event': event,
        'organizer_profile': organizer_profile,
        'user_booking': user_booking,
    }
    return render(request, 'events/event_detail.html', context)

@login_required(login_url='login')
def create_event(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    
    if user_profile.role != 'organizer' and not request.user.is_staff:
        messages.error(request, 'Only organizers can create events.')
        return redirect('home')
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.available_seats = event.seats
            event.save()
            messages.success(request, 'Event created successfully! Awaiting admin approval.')
            return redirect('event-detail', pk=event.pk)
    else:
        form = EventForm()
    
    context = {'form': form}
    return render(request, 'events/event_form.html', context)

@login_required(login_url='login')
def edit_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    if event.organizer != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to edit this event.')
        return redirect('event-detail', pk=event.pk)
    
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully.')
            return redirect('event-detail', pk=event.pk)
    else:
        form = EventForm(instance=event)
    
    context = {'form': form, 'event': event}
    return render(request, 'events/event_form.html', context)

@login_required(login_url='login')
def delete_event(request, pk):
    event = get_object_or_404(Event, pk=pk)
    
    if event.organizer != request.user and not request.user.is_staff:
        messages.error(request, 'You do not have permission to delete this event.')
        return redirect('event-detail', pk=event.pk)
    
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully.')
        return redirect('event-list')
    
    context = {'event': event}
    return render(request, 'events/event_confirm_delete.html', context)

@login_required(login_url='login')
def organizer_events(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    
    if user_profile.role != 'organizer' and not request.user.is_staff:
        messages.error(request, 'Only organizers can view this page.')
        return redirect('home')
    
    events = Event.objects.filter(organizer=request.user)
    context = {'events': events}
    return render(request, 'events/organizer_events.html', context)
