from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('quantity', 'notes')
    
    def __init__(self, *args, **kwargs):
        event = kwargs.pop('event', None)
        super().__init__(*args, **kwargs)
        
        self.fields['quantity'].widget.attrs.update({'class': 'form-control', 'type': 'number', 'min': '1', 'max': event.available_seats if event else '100'})
        self.fields['notes'].widget.attrs.update({'class': 'form-control', 'rows': 3, 'placeholder': 'Additional notes (optional)'})
        
        if event:
            self.fields['quantity'].help_text = f"Available seats: {event.available_seats}"
