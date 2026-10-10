from django import forms
from .models import QuoteRequest, ContactMessage


class QuoteRequestForm(forms.ModelForm):
    class Meta:
        model = QuoteRequest
        fields = [
            'full_name', 'email', 'phone', 'project_type', 
            'estimated_budget', 'property_size', 'timeframe', 
            'site_location', 'message'
        ]
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'John Doe',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'john@example.com',
                'required': 'required'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '+1 (555) 000-1234',
                'required': 'required'
            }),
            'project_type': forms.Select(attrs={
                'class': 'form-select',
                'required': 'required'
            }),
            'estimated_budget': forms.Select(attrs={
                'class': 'form-select',
                'required': 'required'
            }),
            'property_size': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 3,500 sq ft / 2 Floors'
            }),
            'timeframe': forms.Select(attrs={
                'class': 'form-select'
            }),
            'site_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 124 King Street, Downtown'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describe your architectural requirements, site conditions, target timeline...',
                'required': 'required'
            }),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Full Name',
                'required': 'required'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email Address',
                'required': 'required'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone Number (optional)'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'What can we help you build?',
                'required': 'required'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Please give details about your project or general query...',
                'required': 'required'
            }),
        }
