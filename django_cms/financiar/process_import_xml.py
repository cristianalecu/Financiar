import os.path
from pathlib import Path
import xml.etree.ElementTree as ET

from financiar.models import SalesData, Location, ConstNetwork, Benchmark,\
    SalesConcept, SalesConceptSize, Channel, Brand, Category, Subcategory
from django.db import connection

class SalesXmlProcessor():
    
    def __init__(self):
#         SalesData.objects.all().delete()
#         Location.objects.all().delete()
#         Channel.objects.all().delete()
#         Brand.objects.all().delete()
#         Category.objects.all().delete()
#         Subcategory.objects.all().delete()
#         Benchmark.objects.all().delete()
#         SalesConcept.objects.all().delete()
#         SalesConceptSize.objects.all().delete()
#         ConstNetwork.objects.all().delete()
        self.sales_data = SalesData.objects.all()
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
        else:
            obj = obj[0]
            
        return obj
    
    def add_sales_data(self, year, month, value, open):
        self.sales_data.create( 
            location = self.location,
            channel = self.channel,
            brand = self.brand,
            category = self.category,
            subcategory = self.subcategory,
            ebenchmark = self.ebenchmark,
            bbenchmark = self.bbenchmark,
            sales_concept = self.sales_concept,
            sales_concept_size = self.sales_concept_size,
            cn_vs_H = self.cn_vs_H,
            cn_vs_B = self.cn_vs_B,
            year = year,
            month = month,
            open = open,
            value = value,
            user = self.user
            )
    
    def process_xml_if_exists(self, xml_filename, user):
        cwd = os.getcwd()
        my_file = Path(os.path.join(cwd,xml_filename))
        if my_file.is_file():
            first_row = 1
            tree = ET.parse(os.path.join(cwd,xml_filename))
            root = tree.getroot()
            self.user = user;
            for Worksheet in root.iter('{urn:schemas-microsoft-com:office:spreadsheet}Worksheet'):
                for Table in Worksheet.iter('{urn:schemas-microsoft-com:office:spreadsheet}Table'):
                    for Row in Table.iter('{urn:schemas-microsoft-com:office:spreadsheet}Row'):
                        values = []
                        coll = 0
                        if first_row :
                            first_row = 0
                        else:
                            for Cell in Row:
                                for Data in Cell.iter('{urn:schemas-microsoft-com:office:spreadsheet}Data'):
                                    if Data.text is not None:
                                        values.insert(coll,  Data.text)
                                    else:
                                        values.insert(coll,  "")
                                coll = coll + 1
                            if(values[0] == ""):
                                break    
                            if(Worksheet.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Name']=='Sales base'):
                                self.location = self.get_object_by_name(values[2], self.locations, Location)
                                self.cn_vs_H = self.get_object_by_name(values[3], self.constnetworks, ConstNetwork)
                                self.cn_vs_B = self.get_object_by_name(values[4], self.constnetworks, ConstNetwork)
                                self.ebenchmark = self.get_object_by_name(values[5], self.benchmarks, Benchmark)
                                self.bbenchmark = self.get_object_by_name(values[6], self.benchmarks, Benchmark)
                                self.sales_concept = self.get_object_by_name(values[7], self.sales_concepts, SalesConcept)
                                self.sales_concept_size = self.get_object_by_name(values[8], self.sales_concept_sizes, SalesConceptSize)
                                self.channel = self.get_object_by_name(values[9], self.channels, Channel)
                                self.brand = self.get_object_by_name(values[10], self.brands, Brand)
                                self.category = self.get_object_by_name(values[12], self.categories, Category)
                                self.subcategory = self.get_object_by_name(values[13], self.subcategories, Subcategory)
                                self.add_sales_data(2016, 1,  float(values[14]), False)
                                self.add_sales_data(2016, 2,  float(values[15]), False)
                                self.add_sales_data(2016, 3,  float(values[16]), False)
                                self.add_sales_data(2016, 4,  float(values[17]), False)
                                self.add_sales_data(2016, 5,  float(values[18]), False)
                                self.add_sales_data(2016, 6,  float(values[19]), False)
                                self.add_sales_data(2016, 7,  float(values[20]), False)
                                self.add_sales_data(2016, 8,  float(values[21]), False)
                                self.add_sales_data(2016, 9,  float(values[22]), False)
                                self.add_sales_data(2016, 10, float(values[23]), False)
                                self.add_sales_data(2016, 11, float(values[24]), False)
                                self.add_sales_data(2016, 12, float(values[25]), False)
                                self.add_sales_data(2017, 1,  float(values[26]), values[54]>'0')
                                self.add_sales_data(2017, 2,  float(values[27]), values[55]>'0')
                                self.add_sales_data(2017, 3,  float(values[28]), values[56]>'0')
                                self.add_sales_data(2017, 4,  float(values[29]), values[57]>'0')
                                self.add_sales_data(2017, 5,  float(values[30]), values[58]>'0')
                                self.add_sales_data(2017, 6,  float(values[31]), values[59]>'0')
                                self.add_sales_data(2017, 7,  float(values[32]), values[60]>'0')
                                self.add_sales_data(2017, 8,  float(values[33]), values[61]>'0')
                                self.add_sales_data(2017, 9,  float(values[34]), values[62]>'0')
                                self.add_sales_data(2017, 10, float(values[35]), values[63]>'0')
                                self.add_sales_data(2017, 11, float(values[36]), values[64]>'0')
                                self.add_sales_data(2017, 12, float(values[37]), values[65]>'0')
                                self.add_sales_data(2018, 1,  float(values[38]), values[66]>'0')
                                self.add_sales_data(2018, 2,  float(values[39]), values[67]>'0')
                                self.add_sales_data(2018, 3,  float(values[40]), values[68]>'0')
                                self.add_sales_data(2018, 4,  float(values[41]), values[69]>'0')
                                self.add_sales_data(2018, 5,  float(values[42]), values[70]>'0')
                                self.add_sales_data(2018, 6,  float(values[43]), values[71]>'0')
                                self.add_sales_data(2018, 7,  float(values[44]), values[72]>'0')
                                self.add_sales_data(2018, 8,  float(values[45]), values[73]>'0')
                                self.add_sales_data(2018, 9,  float(values[46]), values[74]>'0')
                                self.add_sales_data(2018, 10, float(values[47]), values[75]>'0')
                                self.add_sales_data(2018, 11, float(values[48]), values[76]>'0')
                                self.add_sales_data(2018, 12, float(values[49]), values[77]>'0')
                            elif(Worksheet.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Name']=='Traffic'):
                                self.location = self.get_object_by_name(values[0], self.locations, Location)
                                self.location.number = int(float(self.location.name))
                                self.location.title = values[1]
                                self.location.save()
                                cursor = connection.cursor()
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[9]), self.location.id,2017, 8))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[10]), self.location.id,2017, 9))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[11]), self.location.id,2017, 10))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[12]), self.location.id,2017, 11))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[13]), self.location.id,2017, 12))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[14]), self.location.id,2018, 1))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[15]), self.location.id,2018, 2))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[16]), self.location.id,2018, 3))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[17]), self.location.id,2018, 4))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[18]), self.location.id,2018, 5))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[19]), self.location.id,2018, 6))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[20]), self.location.id,2018, 7))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[21]), self.location.id,2018, 8))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[22]), self.location.id,2018, 9))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[23]), self.location.id,2018, 10))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[24]), self.location.id,2018, 11))
                                cursor.execute("UPDATE financiar_salesdata SET traffic = %f where location_id=%d and year=%d and month=%d", (float(values[25]), self.location.id,2018, 12))
                                
                if(Worksheet.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Name']=='Sales base'):
                    self.locations.save()                                             
                    self.channels.save()                                             
                    self.brands.save()
                    self.categories.save()
                    self.subcategories.save()
                    self.benchmarks.save()
                    self.sales_concepts.save()
                    self.sales_concept_sizes.save()
                    self.constnetworks.save()
                    self.sales_data.save()
