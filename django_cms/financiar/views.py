from django.shortcuts import render
from financiar.forms import SalesDataForm
from django.shortcuts import render, redirect, get_object_or_404
from financiar.models import SalesData, Location, ChannelBrandIndicator,\
    CBIndicatorData, LocationFull, Lookup, CBIndicatorFull
from financiar.process_import_xml import SalesXmlProcessor
import time


def locations_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    processor = SalesXmlProcessor()
    processor.process_xml_if_exists("sales.xml", request.user)
    processor.process_xml_if_exists("trafic_maturity.xml", request.user)
    processor.process_xml_if_exists("trend.xml", request.user)

    thead=['Location_Name','CN_vs._H','CN_vs._B','E Benchmark','B Benchmark','Sales Concept','Sales Concept Size',
           'Channel','Brand','Category','Subcategory']
    table = {}
    for location in LocationFull.objects.raw("select l.id, l.name, l.number, l.title, ch.name channel, b.name brand, c.name category, s.name subcategory, eb.name ebenchmark, bb.name bbenchmark, "
            "sc.name sales_concept, scs.name sales_concept_size, cvh.name cn_vs_H, cvb.name cn_vs_B from financiar_location l "
            "left join financiar_channel ch on ch.id = l.channel_id "
            "left join financiar_brand b on b.id = l.brand_id "
            "left join financiar_category c on c.id = l.category_id "
            "left join financiar_subcategory s on s.id = l.subcategory_id "
            "left join financiar_benchmark eb on eb.id = l.ebenchmark_id "
            "left join financiar_benchmark bb on bb.id = l.bbenchmark_id "
            "left join financiar_salesconcept sc on sc.id = l.sales_concept_id "
            "left join financiar_salesconceptsize scs on scs.id = l.sales_concept_size_id "
            "left join financiar_constnetwork cvh on cvh.id = l.cn_vs_H_id "
            "left join financiar_constnetwork cvb on cvb.id = l.cn_vs_B_id "
            "order by l.number "):        
        table[location.id] = [location.name.zfill(3) + " - " + location.title, location.cn_vs_H, location.cn_vs_B, location.ebenchmark, location.bbenchmark, 
                                   location.sales_concept, location.sales_concept_size,
                                   location.channel, location.brand, location.category, location.subcategory]
        
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Tobacco Locations " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
        'link_new': 'financiar:location_new',
        'link_edit': 'financiar:location_edit',
        'link_delete': 'financiar:location_delete',
    }
    return render(request, 'table_datasort.html', context)

def location_new(request):
    if not request.user.is_staff():
        return redirect('users:login')
    
def location_edit(request):
    if not request.user.is_staff():
        return redirect('users:login')
    
def location_delete(request):
    if not request.user.is_staff():
        return redirect('users:login')
    
def salesdata_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    
    thead=['Location_Name']
    table = {}
    for location in Lookup.objects.raw("select number id, title name from financiar_location order by number"):
        table[location.id] = [str(location.id).zfill(3) + " - " + location.name]
    sales = SalesData.objects.all().only('location_id', 'year', 'month', 'value').order_by('location_id', 'year', 'month')
        
    location = -1
    firstline = 0
    for sale in sales:
        if location != sale.location_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                firstline = 2
            location = sale.location_id
        if firstline == 1:
            thead.append(str(sale.month)+'.'+str(sale.year))
        table[sale.location_id].append(str(sale.value))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Tobacco sales base " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def opens_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    
    thead=['Location_Name']
    table = {}
    for location in Lookup.objects.raw("select number id, title name from financiar_location order by number"):
        table[location.id] = [str(location.id).zfill(3) + " - " + location.name]
    sales = SalesData.objects.all().only('location_id', 'year', 'month', 'open').order_by('location_id', 'year', 'month')
        
    location = -1
    firstline = 0
    for sale in sales:
        if location != sale.location_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                firstline = 2
            location = sale.location_id
        if firstline == 1:
            thead.append(str(sale.month)+'.'+str(sale.year))
        table[sale.location_id].append("1" if sale.open else "0")
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Tobacco opens " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def traffic_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    
    thead=['Location_Name']
    table = {}
    for location in Lookup.objects.raw("select number id, title name from financiar_location order by number"):
        table[location.id] = [str(location.id).zfill(3) + " - " + location.name]
    sales = SalesData.objects.all().only('location_id', 'year', 'month', 'traffic').order_by('location_id', 'year', 'month')
        
    location = -1
    firstline = 0
    for sale in sales:
        if location != sale.location_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                firstline = 2
            location = sale.location_id
        if firstline == 1:
            thead.append(str(sale.month)+'.'+str(sale.year))
        table[sale.location_id].append(str(sale.traffic))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Traffic " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def indicators_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    
    thead=['Indicator', 'Channel','Brand','Category','Subcategory']
    table = {}
    for indicator in CBIndicatorFull.objects.raw("select i.id, i.name, ch.name channel, b.name brand, c.name category, s.name subcategory  from financiar_channelbrandindicator i "
            "left join financiar_brand b on b.id = i.brand_id "
            "left join financiar_channel ch on ch.id = i.channel_id "
            "left join financiar_category c on c.id = i.category_id "
            "left join financiar_subcategory s on s.id = i.subcategory_id "
            "order by i.id"
            ):
        table[indicator.id] = [str(indicator.id), indicator.channel, indicator.brand, indicator.category, indicator.subcategory]
        
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Channel Brand indicators " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def trends_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    
    thead=['Indicator_Channel_Brand']
    table = {}
    for indicator in Lookup.objects.raw("select id, name from financiar_channelbrandindicator order by id"):
        table[indicator.id] = [str(indicator.id).zfill(2) + "-" + indicator.name]
    cbindicatorsdata = CBIndicatorData.objects.all().only('indicator_id', 'year', 'month', 'trend').order_by('indicator_id', 'year', 'month')
        
    indicator = -1
    firstline = 0
    for cbindicator in cbindicatorsdata:
        if indicator != cbindicator.indicator_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                firstline = 2
            indicator = cbindicator.indicator_id
        if firstline == 1:
            thead.append(str(cbindicator.month)+'.'+str(cbindicator.year))
        table[cbindicator.indicator_id].append(str(cbindicator.trend))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Trends " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def inflation_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    
    thead=['Indicator_Channel_Brand']
    table = {}
    for indicator in Lookup.objects.raw("select id, name from financiar_channelbrandindicator order by id"):
        table[indicator.id] = [str(indicator.id).zfill(2) + "-" + indicator.name]
    cbindicatorsdata = CBIndicatorData.objects.all().only('indicator_id', 'year', 'month', 'inflation').order_by('indicator_id', 'year', 'month')
        
    indicator = -1
    firstline = 0
    for cbindicator in cbindicatorsdata:
        if indicator != cbindicator.indicator_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                firstline = 2
            indicator = cbindicator.indicator_id
        if firstline == 1:
            thead.append(str(cbindicator.month)+'.'+str(cbindicator.year))
        table[cbindicator.indicator_id].append(str(cbindicator.inflation))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Inflation " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def actions_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    
    thead=['Indicator_Channel_Brand']
    table = {}
    for indicator in Lookup.objects.raw("select id, name from financiar_channelbrandindicator order by id"):
        table[indicator.id] = [str(indicator.id).zfill(2) + "-" + indicator.name]
    cbindicatorsdata = CBIndicatorData.objects.all().only('indicator_id', 'year', 'month', 'commercial_actions').order_by('indicator_id', 'year', 'month')
        
    indicator = -1
    firstline = 0
    for cbindicator in cbindicatorsdata:
        if indicator != cbindicator.indicator_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                firstline = 2
            indicator = cbindicator.indicator_id
        if firstline == 1:
            thead.append(str(cbindicator.month)+'.'+str(cbindicator.year))
        table[cbindicator.indicator_id].append(str(cbindicator.commercial_actions))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Commercial actions " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)
# <table id="table"
#            data-toggle="table"
#            data-toolbar="#toolbar"
#            data-height="460"
#            data-pagination="true"
#            data-side-pagination="server"
#            data-url="../json/data2.json">
# <th data-field="id" data-sortable="true">ID</th>