from django.shortcuts import render
from financiar.models import SalesData
from financiar.forms import SalesDataForm

def salesdata_list(request):
    if request.user.is_authenticated:
        sales = SalesData.objects.filter(year=2017)
        #sales_form = SalesDataForm() 
        
    context = {
        'page_title': "Tobacco sales",
        'sales': sales,
        #'sales_form': sales_form,
    }
    return render(request, 'table_datasort.html', context)
