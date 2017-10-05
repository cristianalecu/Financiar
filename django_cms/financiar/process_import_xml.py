import os.path
from pathlib import Path
import xml.etree.ElementTree as ET

from financiar.models import SalesData, Location, ConstNetwork, Benchmark,\
    SalesConcept, SalesConceptSize, Channel, Brand, Category, Subcategory

class SalesXmlProcessor():
    
    location = ""
    
    def __init__(self):
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
                    SalesData.objects.all().delete()
                    for Row in Table.iter('{urn:schemas-microsoft-com:office:spreadsheet}Row'):
                        if first_row :
                            first_row = 0
                        else:
                            for Cell in Row:
                                coll = coll + 1
                                for Data in Cell.iter('{urn:schemas-microsoft-com:office:spreadsheet}Data'):
                                    table += " " + Data.tag # + " " + Cell.text # +  " " + Cell.attrib
                                    if coll == 3:
                                        self.location = self.get_object_by_name(Data.text, self.locations, Location)
                                    elif coll == 4:
                                        self.cn_vs_H = self.get_object_by_name(Data.text, self.constnetworks, ConstNetwork)
                                    elif coll == 5:
                                        self.cn_vs_B = self.get_object_by_name(Data.text, self.constnetworks, ConstNetwork)
                                    elif coll == 6:
                                        self.ebenchmark = self.get_object_by_name(Data.text, self.benchmarks, Benchmark)
                                    elif coll == 7:
                                        self.bbenchmark = self.get_object_by_name(Data.text, self.benchmarks, Benchmark)
                                    elif coll == 8:
                                        self.sales_concept = self.get_object_by_name(Data.text, self.sales_concepts, SalesConcept)
                                    elif coll == 9:
                                        self.sales_concept_size = self.get_object_by_name(Data.text, self.sales_concept_sizes, SalesConceptSize)
                                    elif coll == 10:
                                        self.channel = self.get_object_by_name(Data.text, self.channels, Channel)
                                    elif coll == 11:
                                        self.brand = self.get_object_by_name(Data.text, self.brands, Brand)
                                    elif coll == 13:
                                        self.category = self.get_object_by_name(Data.text, self.categories, Category)
                                    elif coll == 14:
                                        self.subcategory = self.get_object_by_name(Data.text, self.subcategories, Subcategory)
                                    elif coll == 15:
                                        self.year=2016 
                                        self.month = 1
                                        self.insert()
                                
                            sales = SalesData.objects.create()
                            sales.save()