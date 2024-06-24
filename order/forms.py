from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('West', 'West'),
		('East', 'East'),
	)

	DISCRICT_CHOICES = (
		('Bhavnagar', 'Bhavnagar'),
		('Dholera', 'Dholera'), 
		('Gaziabad', 'Gaziabad'),
		('Jaipur', 'Jaipur'),
		('Kolakata', 'Kolakata'),
		('Ahmedabad', 'Ahmedabad'),
		('Gariyadhar', 'Gariyadhar'),
		('Baroda', 'Baroda'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Cash On Delivery', 'Cash On Delivery'),
		('Pay using UPI on Delivery','Pay using UPI on Delivery'),
	)

	division = forms.ChoiceField(choices=DIVISION_CHOICES)
	district =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'division', 'district', 'zip_code', 'payment_method']
