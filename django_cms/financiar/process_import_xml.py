import os.path
from pathlib import Path
import xml.etree.ElementTree as ET

from financiar.models import SalesData, Location, ConstNetwork, Benchmark,\
    SalesConcept, SalesConceptSize, Channel, Brand, Category, Subcategory

class SalesXmlProcessor():
    
    def __init__(self):
        self.sales
        self.locations = Location.objects.all()
        self.channels = Channel.objects.all()
        self.brands = Brand.objects.all()
        self.categories = Category.objects.all()
        self.subcategories = Subcategory.objects.all()
        self.benchmarks = Benchmark.objects.all()
        self.sales_concepts = SalesConcept.objects.all()
        self.sales_concept_sizes = SalesConceptSize.objects.all()
        self.constnetworks = ConstNetwork.objects.all()
        
    def get_object_by_name(self, attr_name, objects, classname):
        obj = objects.filter(name=attr_name)
        if obj.count() == 0 :
            obj = classname.objects.create(name=attr_name)
            obj.save()
            objects = classname.objects.all()
        else:
            obj = obj[0]
            
        return obj
    
    def add_sales_data(self, year, month, value, open):
        
    
    def process_xml_if_exists(self, xml_filename):
        cwd = os.getcwd()
        my_file = Path(os.path.join(cwd,xml_filename))
        if my_file.is_file():
            table  = ""
            first_row = 1
            coll = 0
            tree = ET.parse(os.path.join(cwd,xml_filename))
            root = tree.getroot()
            for Worksheet in root.iter('{urn:schemas-microsoft-com:office:spreadsheet}Worksheet'):
                for Table in Worksheet.iter('{urn:schemas-microsoft-com:office:spreadsheet}Table'):
                    sale_data = SalesData.objects.all()
                    values = []
                    for Row in Table.iter('{urn:schemas-microsoft-com:office:spreadsheet}Row'):
                        if first_row :
                            first_row = 0
                        else:
                            for Cell in Row:
                                for Data in Cell.iter('{urn:schemas-microsoft-com:office:spreadsheet}Data'):
                                    if Data.text is not None:
                                        values[coll] = Data.text
                                    else:
                                        values[coll] = ""
                                coll = coll + 1
                                self.location = self.get_object_by_name(values[3], self.locations, Location)
                                self.cn_vs_H = self.get_object_by_name(values[4], self.constnetworks, ConstNetwork)
                                self.cn_vs_B = self.get_object_by_name(values[5], self.constnetworks, ConstNetwork)
                                self.ebenchmark = self.get_object_by_name(values[6], self.benchmarks, Benchmark)
                                self.bbenchmark = self.get_object_by_name(values[7], self.benchmarks, Benchmark)
                                self.sales_concept = self.get_object_by_name(values[8], self.sales_concepts, SalesConcept)
                                self.sales_concept_size = self.get_object_by_name(values[9], self.sales_concept_sizes, SalesConceptSize)
                                self.channel = self.get_object_by_name(values[10], self.channels, Channel)
                                self.brand = self.get_object_by_name(values[11], self.brands, Brand)
                                self.category = self.get_object_by_name(values[13], self.categories, Category)
                                self.subcategory = self.get_object_by_name(values[14], self.subcategories, Subcategory)
                                self.add_sales_data
                                self.year=2016 
                                self.month = 1
                                self.value=float(values[15])
                                self.open=bool(values[55])
                                sale_data.objects.add(location = )
                                
                            sales = SalesData.objects.create()
                            sales.save()