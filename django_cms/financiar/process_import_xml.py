import os.path
from pathlib import Path
import xml.etree.ElementTree as ET

from financiar.models import SalesData, Location, ConstNetwork, Benchmark,\
    SalesConcept, SalesConceptSize, Channel, Brand, Category, Subcategory

class SalesXmlProcessor():
    
    location = ""
    
    def __init__(self):
        self.locations = Location.objects.all()
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
                    locations = Location.objects.all()
                    Location.objects.all().delete()
                    locations = Location.objects.all()
                    for Row in Table.iter('{urn:schemas-microsoft-com:office:spreadsheet}Row'):
                        if first_row :
                            first_row = 0
                        else:
                            for Cell in Row:
                                coll = coll + 1
                                for Data in Cell.iter('{urn:schemas-microsoft-com:office:spreadsheet}Data'):
                                    table += " " + Data.tag # + " " + Cell.text # +  " " + Cell.attrib
                                    if coll == 3:
                                        location = self.get_object_by_name(Data.text,locations, Location)
                                    if coll == 4:
                                        cn_vs_H = ConstNetwork.objects.filter(name=Data.text)
                                        if cn_vs_H.count() == 0 :
                                            cn_vs_H = ConstNetwork.objects.create(name=Data.text)
                                            cn_vs_H.save()
                                        else:
                                            cn_vs_H = cn_vs_H[0]
                                    if coll == 5:
                                        cn_vs_B = ConstNetwork.objects.filter(name=Data.text)
                                        if cn_vs_B.count() == 0 :
                                            cn_vs_B = ConstNetwork.objects.create(name=Data.text)
                                            cn_vs_B.save()
                                        else:
                                            cn_vs_B = cn_vs_B[0]
                                    if coll == 6:
                                        ebenchmark = Benchmark.objects.filter(name=Data.text)
                                        if ebenchmark.count() == 0 :
                                            ebenchmark = Benchmark.objects.create(name=Data.text)
                                            ebenchmark.save()
                                        else:
                                            ebenchmark = ebenchmark[0]
                                    if coll == 7:
                                        bbenchmark = Benchmark.objects.filter(name=Data.text)
                                        if bbenchmark.count() == 0 :
                                            bbenchmark = Benchmark.objects.create(name=Data.text)
                                            bbenchmark.save()
                                        else:
                                            bbenchmark = bbenchmark[0]
                                    if coll == 8:
                                        sales_concept = SalesConcept.objects.filter(name=Data.text)
                                        if sales_concept.count() == 0 :
                                            sales_concept = SalesConcept.objects.create(name=Data.text)
                                            sales_concept.save()
                                        else:
                                            sales_concept = sales_concept[0]
                                    if coll == 9:
                                        sales_concept_size = SalesConceptSize.objects.filter(name=Data.text)
                                        if sales_concept_size.count() == 0 :
                                            sales_concept_size = SalesConceptSize.objects.create(name=Data.text)
                                            sales_concept_size.save()
                                        else:
                                            sales_concept_size = sales_concept_size[0]
                                    if coll == 10:
                                        channel = Channel.objects.filter(name=Data.text)
                                        if channel.count() == 0 :
                                            channel = Channel.objects.create(name=Data.text)
                                            channel.save()
                                        else:
                                            channel = channel[0]
                                    if coll == 11:
                                        brand = Brand.objects.filter(name=Data.text)
                                        if brand.count() == 0 :
                                            brand = Brand.objects.create(name=Data.text)
                                            brand.save()
                                        else:
                                            brand = brand[0]
                                    if coll == 13:
                                        category = Category.objects.filter(name=Data.text)
                                        if category.count() == 0 :
                                            category = Category.objects.create(name=Data.text)
                                            category.save()
                                        else:
                                            category = category[0]
                                    if coll == 14:
                                        subcategory = Subcategory.objects.filter(name=Data.text)
                                        if subcategory.count() == 0 :
                                            subcategory = Subcategory.objects.create(name=Data.text)
                                            subcategory.save()
                                        else:
                                            subcategory = subcategory[0]
                                
                            sales = SalesData.objects.create()
                            sales.save()