from django.forms import ModelForm
from financiar.models import SalesData

class SalesDataForm(ModelForm):

    class Meta:
        model = SalesData
        fields = ('location', 'year', 'month', 'value')