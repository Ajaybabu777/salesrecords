from django import forms
from .models import Salesrecord

class SalesrecordForm(forms.ModelForm):
    totalrevenue = forms.FloatField(disabled=True, required=False)
    totalcost = forms.FloatField(disabled=True, required=False)
    totalprofit = forms.FloatField(disabled=True, required=False)
    class Meta:
        model = Salesrecord
        fields = '__all__'

        widgets = {
            'orderdate': forms.DateInput(attrs={'type': 'date'}),
            'shipdate': forms.DateInput(attrs={'type': 'date'}),
        }