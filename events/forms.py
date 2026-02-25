from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('title', 'description', 'category', 'date', 'time', 'location', 'price', 'seats', 'image')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Event Title'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'rows': 5, 'placeholder': 'Event Description'})
        self.fields['category'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control', 'type': 'date'})
        self.fields['time'].widget.attrs.update({'class': 'form-control', 'type': 'time'})
        self.fields['location'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Event Location'})
        self.fields['price'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Price (INR, 0 for free)'})
        self.fields['seats'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Total Seats Available'})
        self.fields['image'].widget.attrs.update({'class': 'form-control'})

class EventSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search events...'}))
    category = forms.ChoiceField(required=False, choices=[('', 'All Categories')] + list(Event.CATEGORY_CHOICES), widget=forms.Select(attrs={'class': 'form-control'}))
    date_from = forms.DateField(required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    price_max = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max Price (INR)'}))
