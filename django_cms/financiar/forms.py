from django.forms import ModelForm
from financiar.models import Location, ChannelBrandIndicator
from django.forms.widgets import CheckboxSelectMultiple

class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'title', 'channel', 'brand', 'category', 'subcategory', 'ebenchmark', 'bbenchmark', 
                  'sales_concept', 'sales_concept_size', 'cn_vs_H', 'cn_vs_B', 'opened_from', 'opened_to']
        labels = {
            'name': 'Number', 
            'title': 'Name', 
            'channel': 'Channel', 
            'brand': 'Brand', 
            'category': 'Category', 
            'subcategory': 'Subcategory', 
            'ebenchmark': 'E Benchmark', 
            'bbenchmark': 'B Benchmark', 
            'sales_concept': 'Sales Concept', 
            'sales_concept_size': 'Sales Concept Size', 
            'cn_vs_H': 'CN vs H', 
            'cn_vs_B': 'CN vs B', 
            'opened_from': 'Opened since', 
            'opened_to': 'Opened until',
        }
        empty_labels = {
            'channel': 'select a Channel', 
            'brand': 'select a Brand', 
            'category': 'select a Category', 
            'subcategory': 'select a Subcategory', 
            'ebenchmark': 'select a Benchmark', 
            'bbenchmark': 'select a Benchmark', 
            'sales_concept': 'select Sales Concept', 
            'sales_concept_size': 'select Sales Concept Size', 
            'cn_vs_H': 'select Constant Network', 
            'cn_vs_B': 'select Constant Network',
        }
#         help_texts = {
#         }
        widgets = {
            #'notes': Textarea(attrs={'cols': '20', 'rows': '5'}),
        }


class CBIndicatorForm(ModelForm):

    class Meta:
        model = ChannelBrandIndicator
        fields = ['name', 'bchannel', 'channels', 'bbrand', 'brands', 'bcategory', 'categories', 'bsubcategory', 'subcategories', 
                  'bbenchmark', 'ebenchmarks', 'bsalesconcept', 'salesconcepts', 'bsalesconceptsize', 'salesconceptsizes']
        defults = {
            'bchannel': 0,
            'bbrand': 0,
            'bcategory': 0,
            'bsubcategory': 0,
            'bbenchmark': 0,
            'bsalesconcept': 0,
            'bsalesconceptsize': 0,
        }
        labels = {
            'name': 'Comment Name', 
            'bchannel': 'Only for following channels', 
            'channels': 'Channels', 
            'bbrand': 'Only for following Brands', 
            'brands': 'Brands', 
            'bcategory': 'Only for following Categories', 
            'categories': 'Categories', 
            'bsubcategory': 'Only for following Subcategries', 
            'subcategories': 'Subcategries', 
            'bbenchmark': 'Only for following E Benchmarks', 
            'ebenchmarks': 'E Benchmarks', 
            'bsalesconcept': 'Only for following Sales Concepts', 
            'salesconcepts': "Sales Concepts", 
            'bsalesconceptsize': 'Only for following Sales Concept sizes', 
            'salesconceptsizes': 'Sales Concept sizes'
        }
#         empty_labels = {
#             'channel': 'select a Channel', 
#             'brand': 'select a Brand', 
#             'category': 'select a Category', 
#             'subcategory': 'select a Subcategory', 
#             'ebenchmark': 'select a Benchmark', 
#             'bbenchmark': 'select a Benchmark', 
#             'sales_concept': 'select Sales Concept', 
#             'sales_concept_size': 'select Sales Concept Size', 
#             'cn_vs_H': 'select Constant Network', 
#             'cn_vs_B': 'select Constant Network',
#         }
        help_texts = {
            'channels': ' ',
            'brands': ' ',
            'categories': ' ',
            'subcategories': ' ',
            'ebenchmarks': ' ',
            'salesconcepts': ' ',
            'salesconceptsizes': ' ',
        }
        widgets = {
            'channels': CheckboxSelectMultiple(),
            'brands': CheckboxSelectMultiple(),
            'categories': CheckboxSelectMultiple(),
            'subcategories': CheckboxSelectMultiple(),
            'ebenchmarks': CheckboxSelectMultiple(),
            'salesconcepts': CheckboxSelectMultiple(),
            'salesconceptsizes': CheckboxSelectMultiple(),
        }