from .models import Moeda, EModel
from django import forms


class HomepageForm(forms.Form):
    class Meta:
        model = Moeda
        fields = 'nome'
        widgets = {
            'nome':   forms.Select(attrs={'class': 'form-control'})
        }


class EForm(forms.ModelForm):
    class Meta:
        model = EModel
        fields = ()
        widgets = {'date': forms.DateInput(attrs={'class': 'datepicker'})}

