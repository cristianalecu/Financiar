from django.shortcuts import render
from financiar.forms import SalesDataForm
from django.shortcuts import render, redirect, get_object_or_404
from financiar.models import SalesData
from financiar.process_import_xml import SalesXmlProcessor


def salesdata_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    processor = SalesXmlProcessor()
    processor.process_xml_if_exists("sales.xml", request.user)
    processor.process_xml_if_exists("trafic_maturity.xml", request.user)
    
    sales = SalesData.objects.all()
    #sales_form = SalesDataForm() 
    context = {
        'page_title': "Tobacco sales",
        'table': sales,
        #'sales_form': sales_form,
    }
    return render(request, 'table_datasort.html', context)
