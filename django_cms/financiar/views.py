from django.shortcuts import render
from financiar.forms import SalesDataForm
from django.shortcuts import render, redirect, get_object_or_404
from financiar.models import SalesData, Location, ChannelBrandIndicator,\
    CBIndicatorData
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
    
    locations = Location.objects.all().order_by('number')
    
    thead=['Location','CN_vs._H','CN_vs._B','E Benchmark','B Benchmark','Sales Concept','Sales Concept Size',
           'Channel','Brand','Category','Subcategory']
    table = {}
    for location in locations:
        table.insert(location.id, [str(location), location.cn_vs_H.name, location.cn_vs_B.name, location.ebenchmark.name, location.bbenchmark.name, 
                                   location.sales_concept.name, location.sales_concept_size.name,
                                   location.channel.name, location.brand.name, location.category.name, location.subcategory.name])
        
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Tobacco Locations " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def salesdata_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    
    locations = Location.objects.all().order_by('number')
    sales = SalesData.objects.all().order_by('location_id', 'year', 'month')
    
    thead=['Location']
    table = {}
    for location in locations:
        table.insert(location.id, [str(location)])
        
    location = -1
    firstline = 0
    for sale in sales:
        if location != sale.location_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                    firstline = 2
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
    
    locations = Location.objects.all().order_by('number')
    sales = SalesData.objects.all().order_by('location_id', 'year', 'month')
    
    thead=['Location']
    table = {}
    for location in locations:
        table.insert(location.id, [str(location)])
        
    location = -1
    firstline = 0
    for sale in sales:
        if location != sale.location_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                    firstline = 2
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
    
    locations = Location.objects.all().order_by('number')
    sales = SalesData.objects.all().order_by('location_id', 'year', 'month')
    
    thead=['Location']
    table = {}
    for location in locations:
        table.insert(location.id, [str(location)])
        
    location = -1
    firstline = 0
    for sale in sales:
        if location != sale.location_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                    firstline = 2
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
    
    indicators = ChannelBrandIndicator.objects.all().order_by('id')
    
    thead=['Indicator', 'Channel','Brand','Category','Subcategory']
    table = {}
    for indicator in indicators:
        table.insert(indicator.id, [str(indicator.id), indicator.channel.name, indicator.brand.name, indicator.category.name, indicator.subcategory.name])
        
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
    
    indicators = ChannelBrandIndicator.objects.all().order_by('id')
    cbindicatorsdata = CBIndicatorData.objects.all().order_by('indicator_id', 'year', 'month')
    
    thead=['Indicator']
    table = {}
    for indicator in indicators:
        table.insert(indicator.id, [str(indicator)])
        
    indicator = -1
    firstline = 0
    for cbindicator in cbindicatorsdata:
        if indicator != cbindicator.indicator_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                    firstline = 2
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
    
    indicators = ChannelBrandIndicator.objects.all().order_by('id')
    cbindicatorsdata = CBIndicatorData.objects.all().order_by('indicator_id', 'year', 'month')
    
    thead=['Indicator']
    table = {}
    for indicator in indicators:
        table.insert(indicator.id, [str(indicator)])
        
    indicator = -1
    firstline = 0
    for cbindicator in cbindicatorsdata:
        if indicator != cbindicator.indicator_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                    firstline = 2
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
    
    indicators = ChannelBrandIndicator.objects.all().order_by('id')
    cbindicatorsdata = CBIndicatorData.objects.all().order_by('indicator_id', 'year', 'month')
    
    thead=['Indicator']
    table = {}
    for indicator in indicators:
        table.insert(indicator.id, [str(indicator)])
        
    indicator = -1
    firstline = 0
    for cbindicator in cbindicatorsdata:
        if indicator != cbindicator.indicator_id :
            if firstline == 0:
                firstline = 1
            elif firstline == 1:
                    firstline = 2
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