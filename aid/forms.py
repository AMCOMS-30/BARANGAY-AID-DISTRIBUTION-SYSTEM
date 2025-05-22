from django import forms
from .models import AidApplication, AidType

class AidApplicationForm(forms.ModelForm):
    class Meta:
        model = AidApplication
        fields = ['name', 'address', 'age', 'aid_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input'}),
            'address': forms.TextInput(attrs={'class': 'input'}),
            'age': forms.NumberInput(attrs={'class': 'input'}),
            'aid_type': forms.Select(attrs={'class': 'input'}),
        }
