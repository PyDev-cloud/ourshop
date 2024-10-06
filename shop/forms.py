from django import forms
from .models import Billing  # Ensure you are importing the correct Billing model

class BillingAddressForm(forms.ModelForm):
    class Meta:
        model = Billing  # This should reference your Billing model
        fields = '__all__'  # Include all fields from the Billing model