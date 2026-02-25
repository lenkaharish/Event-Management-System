from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserUpdateForm, UserProfileForm, LoginForm
from .models import UserProfile
from bookings.models import Booking

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Create user profile automatically
            UserProfile.objects.create(user=user)
            messages.success(request, 'Account created successfully! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

@login_required(login_url='login')
def profile(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    bookings = request.user.bookings.all()
    
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = UserProfileForm(instance=user_profile)
    
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'bookings': bookings,
        'user_profile': user_profile
    }
    return render(request, 'accounts/profile.html', context)

@login_required(login_url='login')
def user_dashboard(request):
    user_profile = UserProfile.objects.get_or_create(user=request.user)[0]
    bookings = request.user.bookings.all()
    upcoming_events = Booking.objects.filter(user=request.user, event__date__gte='2025-01-01').count()
    
    context = {
        'user_profile': user_profile,
        'bookings': bookings,
        'total_bookings': bookings.count(),
        'upcoming_events': upcoming_events,
    }
    return render(request, 'accounts/dashboard.html', context)
