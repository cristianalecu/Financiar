from django.shortcuts import render, redirect, get_object_or_404
from financiar.models import SalesData, Location, ChannelBrandIndicator,\
    CBIndicatorData, LocationFull, Lookup, CBIndicatorFull, GraficData
from financiar.process_import_xml import SalesXmlProcessor
import time
import locale
from financiar.forms import CBIndicatorForm


def locations_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/') 
    
    start_time=time.time()
    processor = SalesXmlProcessor()
    processor.process_xml_if_exists("sales.xml", request.user)
    processor.process_xml_if_exists("trafic_maturity.xml", request.user)
    processor.process_xml_if_exists("trend.xml", request.user)
    processor.process_xml_if_exists("opens.xml", request.user)

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
    if not request.user.is_staff:
        return redirect('users:login')
    return redirect('financiar:locations_list')
    
def location_edit(request, pk):
    if not request.user.is_staff:
        return redirect('users:login')
    return redirect('financiar:locations_list')
    
def location_delete(request, pk):
    if not request.user.is_staff:
        return redirect('users:login')
    return redirect('financiar:locations_list')
    
def salesdata_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    locale.setlocale(locale.LC_NUMERIC, 'English')
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
        table[sale.location_id].append(locale.format("%.2f",sale.value,True))
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
    locale.setlocale(locale.LC_NUMERIC, 'English')
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
        table[sale.location_id].append("{0:.2f}%".format(sale.traffic * 100))
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
    locale.setlocale(locale.LC_NUMERIC, 'English')
    thead=['Indicator', 'Channel','Brand','Category','Subcategory', 'Ebenchmarks', 'Sales Concept', 'Sales Concept Size']
    table = {}
    for indicator in ChannelBrandIndicator.objects.all().order_by('id'):
        channels = ""
        brands = ""
        categs = ""
        subcategs = ""
        ebench = ""
        sconcepts = ""
        sconceptsz = ""
        for obj in indicator.channels.all():
            channels += (", " + obj.name)
        for obj in indicator.brands.all():
            brands += (", " + obj.name)
        for obj in indicator.categories.all():
            categs += (", " + obj.name)
        for obj in indicator.subcategories.all():
            subcategs += (", " + obj.name)
        for obj in indicator.ebenchmarks.all():
            ebench += (", " + obj.name)
        for obj in indicator.salesconcepts.all():
            sconcepts += (", " + obj.name)
        for obj in indicator.salesconceptsizes.all():
            sconceptsz += (", " + obj.name)
        if len(channels) > 0 :
            channels = channels[2:]
        if len(brands) > 0 :
            brands = brands[2:]
        if len(categs) > 0 :
            categs = categs[2:]
        if len(subcategs) > 0 :
            subcategs = subcategs[2:]
        if len(ebench) > 0 :
            ebench = ebench[2:]
        if len(sconcepts) > 0 :
            sconcepts = sconcepts[2:]
        if len(sconceptsz) > 0 :
            sconceptsz = sconceptsz[2:]
        table[indicator.id] = [str(indicator.id), channels, brands,categs,subcategs,ebench,sconcepts,sconceptsz]

    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Channel Brand indicators " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
        'link_new': 'financiar:indicator_new',
        'link_edit': 'financiar:indicator_edit',
        'link_delete': 'financiar:indicator_delete',
    }
    return render(request, 'table_datasort.html', context)

def indicator_new(request):
    if not request.user.is_staff:
        return redirect('users:login')
    
    if request.method == "POST":
        form = CBIndicatorForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.update = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
            obj = form.save(commit=True)
            return redirect('financiar:indicators_list')
    else:
        form = CBIndicatorForm()

    context = {
        'page_title': 'New Indicator',
        'form': form,
    }
    return render(request, 'modelform_edit.html', context)
    
def indicator_edit(request, pk):
    if not request.user.is_staff:
        return redirect('users:login')
    
    obj = get_object_or_404(ChannelBrandIndicator, pk=pk)
    if request.method == "POST":
        form = CBIndicatorForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.update = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
            obj = form.save(commit=True)
            return redirect('financiar:indicators_list')
    else:
        form = CBIndicatorForm(instance=obj)

    context = {
        'page_title': 'Indicator '+obj.name,
        'form': form,
    }
    return render(request, 'modelform_edit.html', context)
    
def indicator_delete(request, pk):
    if not request.user.is_staff:
        return redirect('users:login')
    
    obj = get_object_or_404(ChannelBrandIndicator, pk=pk)
    obj.delete()
    return redirect('financiar:indicators_list')

def trends_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    locale.setlocale(locale.LC_NUMERIC, 'English')
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
        table[cbindicator.indicator_id].append("{0:.2f}%".format(cbindicator.trend * 100))
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
    locale.setlocale(locale.LC_NUMERIC, 'English')
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
        table[cbindicator.indicator_id].append("{0:.2f}%".format(cbindicator.inflation * 100))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Inflation " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def trend_impact_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    locale.setlocale(locale.LC_NUMERIC, 'English')
    thead=['Location_Name']
    table = {}
    for location in Lookup.objects.raw("select number id, title name from financiar_location order by number"):
        table[location.id] = [str(location.id).zfill(3) + " - " + location.name]
    sales = SalesData.objects.raw("select s.id, s.location_id, s.year, s.month, s.open, s.matur, "
            "CASE WHEN l.ebenchmark_id in (select b.id from financiar_benchmark b where name='m-o-m' or name='m-o-pm')  THEN "
            "  s.value * COALESCE(cb.trend, 0) else 0 end value, "
            "  s.traffic, s.updated, s.user_id, s.type from financiar_salesdata s "
            "left join financiar_location l on l.id = s.location_id "
            "left outer join financiar_channelbrandindicator ind "
            "      on ind.channel_id = l.channel_id and ind.brand_id = l.brand_id and ind.category_id=l.category_id and ind.subcategory_id=l.subcategory_id "
            "left outer join financiar_cbindicatordata cb on ind.id = cb.indicator_id and s.year=cb.year and s.month = cb.month "
            "order by s.location_id, s.year, s.month")
        
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
        table[sale.location_id].append(locale.format("%.0f",sale.value,True))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Tobacco Trend impact " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def traffic_impact_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    locale.setlocale(locale.LC_NUMERIC, 'English')
    thead=['Location_Name']
    table = {}
    for location in Lookup.objects.raw("select number id, title name from financiar_location order by number"):
        table[location.id] = [str(location.id).zfill(3) + " - " + location.name]
    sales = SalesData.objects.raw("select s.id, s.location_id, s.year, s.month, s.open, s.matur, "
            "CASE WHEN l.ebenchmark_id in (select b.id from financiar_benchmark b where name='m-o-m' or name='m-o-pm')  THEN "
            "  s.value * s.traffic else 0 end value, "
            "  s.traffic, s.updated, s.user_id, s.type from financiar_salesdata s "
            "left join financiar_location l on l.id = s.location_id "
            "order by s.location_id, s.year, s.month")
        
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
        table[sale.location_id].append(locale.format("%.0f",sale.value,True))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Tobacco Traffic impact " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def finalsales_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    locale.setlocale(locale.LC_NUMERIC, 'English')
    thead=['Location_Name']
    table = {}
    for location in Lookup.objects.raw("select number id, title name from financiar_location order by number"):
        table[location.id] = [str(location.id).zfill(3) + " - " + location.name]
    sales = SalesData.objects.raw("select s.id, s.location_id, s.year, s.month, s.open, s.matur, "
            " s.value * (1+coalesce(cb.trend,0)+coalesce(cb.inflation,0)+coalesce(cb.commercial_actions,0)-s.matur + (coalesce(cb.trend,0)+coalesce(cb.inflation,0)+coalesce(cb.commercial_actions,0)-s.matur) * s.traffic) value,  "
            " s.traffic, s.updated, s.user_id, s.type from financiar_salesdata s "
            " left join financiar_location l on l.id = s.location_id "
            " left outer join financiar_channelbrandindicator ind "
            "  on   (ind.bchannel=0 or exists (select id from financiar_channelbrandindicator_channels cbch where ind.id=cbch.channelbrandindicator_id and cbch.channel_id=l.channel_id) ) "
            "   and (ind.bbrand=0 or exists (select id from financiar_channelbrandindicator_brands cbbr where ind.id=cbbr.channelbrandindicator_id and cbbr.brand_id=l.brand_id) ) "
            "   and (ind.bcategory=0 or exists (select id from financiar_channelbrandindicator_categories cbc where ind.id=cbc.channelbrandindicator_id and cbc.category_id=l.category_id) ) "
            "   and (ind.bsubcategory=0 or exists (select id from financiar_channelbrandindicator_subcategories cbsu where ind.id=cbsu.channelbrandindicator_id and cbsu.subcategory_id=l.subcategory_id) ) "
            "   and (ind.bbenchmark=0 or exists (select id from financiar_channelbrandindicator_ebenchmarks cbbe where ind.id=cbbe.channelbrandindicator_id and cbbe.benchmark_id=l.ebenchmark_id) ) "
            "   and (ind.bsalesconcept=0 or exists (select id from financiar_channelbrandindicator_salesconcepts cbs where ind.id=cbs.channelbrandindicator_id and cbs.salesconcept_id=l.sales_concept_id) ) "
            "   and (ind.bsalesconceptsize=0 or exists (select id from financiar_channelbrandindicator_salesconceptsizes cbss where ind.id=cbss.channelbrandindicator_id and cbss.salesconceptsize_id=l.sales_concept_size_id) ) "
            "left outer join financiar_cbindicatordata cb on ind.id = cb.indicator_id and s.year=cb.year and s.month = cb.month "
            "order by s.location_id, s.year, s.month")
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
        table[sale.location_id].append(locale.format("%.0f",sale.value,True))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Tobacco Final Sales " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def graffic_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
    
    start_time=time.time()
    locale.setlocale(locale.LC_NUMERIC, 'English')
    thead=['Sum']
    table = {'base':['00 Base'],
             'trend':['01 Trend'],
             'trendprc':['02 Trend%'],
             'infla':['03 Inflation'],
             'inflaprc':['04 Inflation%'],
             'comm':['05 Commercial'],
             'commprc':['06Commercial%'],
             'matur':['07 Maturity'],
             'maturprc':['08 Maturity%'],
             'traffic':['09 Traffic'],
             'trafficprc':['10 Traffic%'],
             'tot':['99 Total'],
             }
    sales = GraficData.objects.raw("select s.year * 12 + s.month id, s.year, s.month, sum(s.value) base, "
"sum(CASE WHEN l.ebenchmark_id in (select b.id from financiar_benchmark b where name='m-o-m' or name='m-o-pm')  THEN s.value * (coalesce(cb.trend,0))  else 0  end) trend, "
"sum(CASE WHEN l.ebenchmark_id in (select b.id from financiar_benchmark b where name='m-o-m' or name='m-o-pm')  THEN s.value * (coalesce(cb.inflation,0))  else 0  end) inflation, "
"sum(CASE WHEN l.ebenchmark_id in (select b.id from financiar_benchmark b where name='m-o-m' or name='m-o-pm')  THEN s.value * (coalesce(cb.commercial_actions,0))  else 0  end) commercial_actions, "
"sum(CASE WHEN l.ebenchmark_id in (select b.id from financiar_benchmark b where name='m-o-m' or name='m-o-pm')  THEN s.value * (s.matur)  else 0  end) matur, "
"sum(CASE WHEN l.ebenchmark_id in (select b.id from financiar_benchmark b where name='m-o-m' or name='m-o-pm')  THEN s.value * ((1-s.matur+coalesce(cb.trend,0)+coalesce(cb.inflation,0)+coalesce(cb.commercial_actions,0)) * s.traffic)  else 0  end) traffic, "
"sum(CASE WHEN l.ebenchmark_id in (select b.id from financiar_benchmark b where name='m-o-m' or name='m-o-pm')  THEN s.value * ((1-s.matur+coalesce(cb.trend,0)+coalesce(cb.inflation,0)+coalesce(cb.commercial_actions,0)) + (-s.matur+coalesce(cb.trend,0)+coalesce(cb.inflation,0)+coalesce(cb.commercial_actions,0)) * s.traffic)  else s.value  end) fullx  "
"from financiar_salesdata s  "
"left join financiar_location l on l.id = s.location_id "
"left outer join financiar_channelbrandindicator ind  "
"      on ind.channel_id = l.channel_id and ind.brand_id = l.brand_id and ind.category_id=l.category_id and ind.subcategory_id=l.subcategory_id  "
"left outer join financiar_cbindicatordata cb on ind.id = cb.indicator_id and s.year=cb.year and s.month = cb.month  "
"where l.cn_vs_B_id=2 "
"group by s.year, s.month     order by s.year, s.month")
        
    for sale in sales:
        thead.append(str(sale.month)+'.'+str(sale.year))
        table['base'].append(locale.format("%.0f",sale.base,True))
        table['trend'].append(locale.format("%.3f",sale.trend,True))
        table['trendprc'].append("{0:.2f}%".format(sale.trend / sale.fullx * 100))
        table['infla'].append(locale.format("%.3f",sale.inflation,True))
        table['inflaprc'].append("{0:.2f}%".format(sale.inflation / sale.fullx * 100))
        table['comm'].append(locale.format("%.3f",sale.commercial_actions,True))
        table['commprc'].append("{0:.2f}%".format(sale.commercial_actions / sale.fullx * 100))
        table['matur'].append(locale.format("%.3f",sale.matur,True))
        table['maturprc'].append("{0:.2f}%".format(sale.matur / sale.fullx * 100))
        table['traffic'].append(locale.format("%.3f",sale.traffic,True))
        table['trafficprc'].append("{0:.2f}%".format(sale.traffic / sale.fullx * 100))
        table['tot'].append(locale.format("%.0f",sale.fullx,True))
    elapsed_time=time.time()-start_time
    context = {
        'page_title': "Tobacco GRAFFIC " + time.strftime("%H:%M:%S", time.gmtime(elapsed_time)),
        'tab_head': thead,
        'tab_body': table,
    }
    return render(request, 'table_datasort.html', context)

def actions_list(request):
    if request.user.id is  None:
        return redirect('/accounts/login/')
       
    start_time=time.time()
    locale.setlocale(locale.LC_NUMERIC, 'English')   
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
        table[cbindicator.indicator_id].append("{0:.2f}%".format(cbindicator.commercial_actions * 100))
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