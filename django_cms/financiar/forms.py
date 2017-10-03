from django.forms import ModelForm
from financiar.models import SalesData

class SalesDataForm(ModelForm):

    class Meta:
        model = SalesData
        fields = ('location', 'channel', 'brand', 'category', 'subcategory', 'sales_concept', 'sales_concept_size', 'ebenchmark', 'bbenchmark', 'cn_vs_H', 'cn_vs_B', 'year', 'month', 'value')