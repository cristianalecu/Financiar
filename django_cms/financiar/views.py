from django.shortcuts import render
from financiar.forms import SalesDataForm
from django.shortcuts import render, redirect, get_object_or_404
from financiar.models import SalesData
from financiar.process_import_xml import SalesXmlProcessor
import time

def salesdata_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    processor = SalesXmlProcessor()
    processor.process_xml_if_exists("sales.xml", request.user)
    processor.process_xml_if_exists("trafic_maturity.xml", request.user)
    
    sales = SalesData.objects.all().order_by('location', 'year', 'month')
    
    thead=['Location','CN_vs._H','CN_vs._B','E Benchmark','B Benchmark','Sales Concept','Sales Concept Size',
           'Channel','Brand','Category','Subcategory']

    table = []
    row=[]
    location = -1
    firstline = 0
    firstcols = False
    even=0
    for sale in sales:
        if location != sale.location_id :
            if firstline == 0:
                firstline = 1
            else:
                table.append(row)
                if firstline == 1:
                    firstline = 2
            location = sale.location_id
            firstcols = True
        if firstcols:
            row = [sale.location_id, sale.cn_vs_H_id, sale.cn_vs_B_id, sale.ebenchmark_id, sale.bbenchmark_id,
                   sale.sales_concept_id, sale.sales_concept_size_id, sale.channel_id, sale.brand_id, sale.category_id, sale.subcategory_id]
            firstcols = False
        if firstline == 1:
            thead.append(str(sale.month)+'.'+str(sale.year))
        row.append(str(sale.value))
    table.append(row)
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Tobacco sales " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)
