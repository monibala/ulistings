from django import forms

# from Category.models import Bookingorder


class bookingform(forms.Form):
    date = forms.DateField(label='date')
    time = forms.TimeField(label='time')
    guests = forms.IntegerField(label='guests')
    # class Meta:
    #     model = Bookingorder
    #     fields = ("date", "time", "guests")