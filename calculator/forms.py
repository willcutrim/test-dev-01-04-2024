from django import forms
from .models import RegrasDeDesconto, Consumer

class RegrasDeDescontoForm(forms.ModelForm):
    class Meta:
        model = RegrasDeDesconto
        fields = ['consumer_type', 'consumption_range', 'cover_value', 'discount_value']



class ConsumerForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = ['name', 'document', 'zip_code', 'city', 'state', 'consumption', 'distributor_tax', 'discount_rule']