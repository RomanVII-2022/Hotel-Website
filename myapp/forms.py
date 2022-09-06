from dataclasses import fields
from random import choices
from tkinter.tix import Select
from django import forms
from .models import Reservation


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


CHOICES = (('1-3 people', '1-3 people'),('4-6 people', '4-6 people'), ('7-9 people', '7-9 people'), ('10-12 people', '10-12 people'), ('13-15 people', '13-15 people'),)
class ReservationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control font-weight-bold", "placeholder":"First Name"}), label="")
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control font-weight-bold", "placeholder":"Last Name"}), label="")
    phone_number = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control font-weight-bold","placeholder":"Phone Number *eg +254712345677*"}), label="")
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control font-weight-bold", "placeholder":"Email"}), label="")
    date = forms.DateField(widget=DateInput(attrs={"class":"form-control font-weight-bold", "placeholder":"Date"}), label="")
    time = forms.TimeField(widget=TimeInput(attrs={"class":"form-control font-weight-bold", "placeholder":"Time"}), label="")
    no_of_people = forms.CharField(widget=forms.Select(choices=CHOICES, attrs={"class":"form-control font-weight-bold", "placeholder":"Number of People"}), label="")
    
    class Meta:
        model = Reservation
        fields = ('first_name', 'last_name', 'phone_number', 'email', 'date', 'time', 'no_of_people')


        