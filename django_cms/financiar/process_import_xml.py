import os.path
from pathlib import Path
import xml.etree.ElementTree as ET

from financiar.models import SalesData, Location, ConstNetwork, Benchmark,\
    SalesConcept, SalesConceptSize, Channel, Brand, Category, Subcategory,\
    CBIndicatorData, ChannelBrandIndicator
from django.db import connection

class SalesXmlProcessor():
    
    def __init__(self):
#         CBIndicatorData.all().delete()
#         ChannelBrandIndicator.all().delete()
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
        self.channels = Channel.objects.all()
        self.brands = Brand.objects.all()
        self.categories = Category.objects.all()
        self.subcategories = Subcategory.objects.all()
        self.benchmarks = Benchmark.objects.all()
        self.sales_concepts = SalesConcept.objects.all()
        self.sales_concept_sizes = SalesConceptSize.objects.all()
        self.constnetworks = ConstNetwork.objects.all()
        self.locations = Location.objects.all()
        self.cbindicators = ChannelBrandIndicator.objects.all()
        
    def get_object_by_name(self, attr_name, objects, classname):
        obj = objects.filter(name=attr_name)
        if obj.count() == 0 :
            obj = classname.objects.create(name=attr_name, user=self.user)
        else:
            obj = obj[0]
            
        return obj
    
    def get_location(self, location):
        obj = self.locations.filter(name=location)
        if obj.count() == 0 :
            obj = Location.objects.create( 
                name = location,
                number = int(location),
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
                user = self.user
                )
        else:
            obj = obj[0]

        return obj
    
    def add_sales_data(self, year, month, value, opened):
        Location.objects.get_or_create( 
            location = self.location,
            year = year,
            month = month,
            open = opened,
            value = value,
            user = self.user
            )
        
    def get_cbindicator(self, channel, brand, category, subcategory):
        name=channel+'/'+brand+'/'+category+'/'+subcategory
        obj = self.cbindicators.filter(name=name)
        if obj.count() == 0 :
            self.channel = self.get_object_by_name(channel, self.channels, Channel)
            self.brand = self.get_object_by_name(brand, self.brands, Brand)
            self.category = self.get_object_by_name(category, self.categories, Category)
            self.subcategory = self.get_object_by_name(subcategory, self.subcategories, Subcategory)
            obj = self.cbindicators.create( 
                name = name,
                channel = self.channel,
                brand = self.brand,
                category = self.category,
                subcategory = self.subcategory,
                user = self.user
                )
        else:
            obj = obj[0]

        return obj
    
    def add_cbindicator_trend(self, year, month, trend):
        CBIndicatorData.objects.get_or_create( 
            indicator = self.cbindicator,
            year = year,
            month = month,
            trend = trend,
            user = self.user
            )
    def add_cbindicator_inflation(self, year, month, inflation):
        obj = self.cbindicator_data.filter(indicator_id=self.cbindicator.id, year=year, month=month)
        if obj.count() == 0 :
            self.cbindicator_data.create( 
                    indicator = self.cbindicator,
                    year = year,
                    month = month,
                    inflation = inflation,
                    user = self.user
                    )
        else:
            obj = obj[0]
            obj.inflation = inflation
            obj.save()
    def add_cbindicator_actions(self, year, month, actions):
        obj = self.cbindicator_data.filter(indicator_id=self.cbindicator.id, year=year, month=month)
        if obj.count() == 0 :
            self.cbindicator_data.create( 
                    indicator = self.cbindicator,
                    year = year,
                    month = month,
                    commercial_actions = actions,
                    user = self.user
                    )
        else:
            obj = obj[0]
            obj.commercial_actions = actions
            obj.save()
    
    def process_xml_if_exists(self, xml_filename, user):
        cwd = os.getcwd()
        my_file = Path(os.path.join(cwd,xml_filename))
        if my_file.is_file():
            tree = ET.parse(os.path.join(cwd,xml_filename))
            root = tree.getroot()
            self.user = user;
            self.cursor = connection.cursor()
            for Worksheet in root.iter('{urn:schemas-microsoft-com:office:spreadsheet}Worksheet'):
                for Table in Worksheet.iter('{urn:schemas-microsoft-com:office:spreadsheet}Table'):
                    first_row = 1
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
                            if(len(values) == 0):
                                break    
                            if(Worksheet.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Name']=='Sales base'):
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
                                self.location = self.get_location(values[2])
#                                 sql_string = "INSERT INTO owner (`id`, `person_id`) VALUES (%s, %s)"
#                                 self.cursor.execute(sql_string, (665, 330))
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
                                self.location = self.get_location(values[1])
                                self.location.title = values[2]
                                self.location.save()
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[3]), self.location.id,2017, 8))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[4]), self.location.id,2017, 9))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[5]), self.location.id,2017, 10))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[6]), self.location.id,2017, 11))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[7]), self.location.id,2017, 12))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[8]), self.location.id,2018, 1))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[9]), self.location.id,2018, 2))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[10]),self.location.id,2018, 3))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[11]),self.location.id,2018, 4))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[12]),self.location.id,2018, 5))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[13]),self.location.id,2018, 6))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[14]),self.location.id,2018, 7))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[15]),self.location.id,2018, 8))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[16]),self.location.id,2018, 9))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[17]),self.location.id,2018, 10))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[18]),self.location.id,2018, 11))
                                self.cursor.execute("UPDATE financiar_salesdata SET traffic = %s where location_id=%s and year=%s and month=%s", (float(values[19]),self.location.id,2018, 12))
                            elif(Worksheet.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Name']=='Opens'):
                                self.location = self.get_location(values[0])
                                for i in range(0,24):
                                    matur = 0
                                    j = 0
                                    if(self.location.ebenchmark_id == 2):
                                        if self.location.id == 360 and i == 18:
                                            matur = 0
                                        if i > 0 and values[i+1] > '0':
                                            for j in range(0, i-1):
                                                if values[j+1] > '0':
                                                    matur += 1
                                            if matur < 12:
                                                matur = 0.2
                                            else:
                                                matur=0.1
                                    self.cursor.execute("UPDATE financiar_salesdata SET open = %s, matur=%s where location_id=%s and year=%s and month=%s", (values[i+1], matur, self.location.id, 2017+int(i/12), i%12+1))

                            elif(Worksheet.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Name']=='Trend'):   
                                self.cbindicator = self.get_cbindicator(values[1], values[2], values[3], values[4])                                
                                if len(values) == 24 :
                                    self.add_cbindicator_trend(2017,4 ,float(values[6]))
                                    self.add_cbindicator_trend(2017,8 ,float(values[7]))
                                    self.add_cbindicator_trend(2017,9 ,float(values[8]))
                                    self.add_cbindicator_trend(2017,10,float(values[9]))
                                    self.add_cbindicator_trend(2017,11,float(values[10]))
                                    self.add_cbindicator_trend(2017,12,float(values[11]))
                                    self.add_cbindicator_trend(2018,1 ,float(values[12]))
                                    self.add_cbindicator_trend(2018,2 ,float(values[13]))
                                    self.add_cbindicator_trend(2018,3 ,float(values[14]))
                                    self.add_cbindicator_trend(2018,4 ,float(values[15]))
                                    self.add_cbindicator_trend(2018,5 ,float(values[16]))
                                    self.add_cbindicator_trend(2018,6 ,float(values[17]))
                                    self.add_cbindicator_trend(2018,7 ,float(values[18]))
                                    self.add_cbindicator_trend(2018,8 ,float(values[19]))
                                    self.add_cbindicator_trend(2018,9 ,float(values[20]))
                                    self.add_cbindicator_trend(2018,10,float(values[21]))
                                    self.add_cbindicator_trend(2018,11,float(values[22]))
                                    self.add_cbindicator_trend(2018,12,float(values[23]))
                                else:
                                    self.add_cbindicator_trend(2017,8 ,float(values[6]))
                                    self.add_cbindicator_trend(2017,9 ,float(values[7]))
                                    self.add_cbindicator_trend(2017,10,float(values[8]))
                                    self.add_cbindicator_trend(2017,11,float(values[9]))
                                    self.add_cbindicator_trend(2017,12,float(values[10]))
                                    self.add_cbindicator_trend(2018,1 ,float(values[11]))
                                    self.add_cbindicator_trend(2018,2 ,float(values[12]))
                                    self.add_cbindicator_trend(2018,3 ,float(values[13]))
                                    self.add_cbindicator_trend(2018,4 ,float(values[14]))
                                    self.add_cbindicator_trend(2018,5 ,float(values[15]))
                                    self.add_cbindicator_trend(2018,6 ,float(values[16]))
                                    self.add_cbindicator_trend(2018,7 ,float(values[17]))
                                    self.add_cbindicator_trend(2018,8 ,float(values[18]))
                                    self.add_cbindicator_trend(2018,9 ,float(values[19]))
                                    self.add_cbindicator_trend(2018,10,float(values[20]))
                                    self.add_cbindicator_trend(2018,11,float(values[21]))
                                    self.add_cbindicator_trend(2018,12,float(values[22]))
                            elif(Worksheet.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Name']=='Inflation'):
                                try:
                                    self.cbindicator_data
                                except NameError:
                                    self.cbindicator_data = CBIndicatorData.objects.all()
                                self.cbindicator = self.get_cbindicator(values[1], values[2], values[3], values[4])                                
                                self.add_cbindicator_inflation(2017,8 ,float(values[6]))
                                self.add_cbindicator_inflation(2017,9 ,float(values[7]))
                                self.add_cbindicator_inflation(2017,10,float(values[8]))
                                self.add_cbindicator_inflation(2017,11,float(values[9]))
                                self.add_cbindicator_inflation(2017,12,float(values[10]))
                                self.add_cbindicator_inflation(2018,1 ,float(values[11]))
                                self.add_cbindicator_inflation(2018,2 ,float(values[12]))
                                self.add_cbindicator_inflation(2018,3 ,float(values[13]))
                                self.add_cbindicator_inflation(2018,4 ,float(values[14]))
                                self.add_cbindicator_inflation(2018,5 ,float(values[15]))
                                self.add_cbindicator_inflation(2018,6 ,float(values[16]))
                                self.add_cbindicator_inflation(2018,7 ,float(values[17]))
                                self.add_cbindicator_inflation(2018,8 ,float(values[18]))
                                self.add_cbindicator_inflation(2018,9 ,float(values[19]))
                                self.add_cbindicator_inflation(2018,10,float(values[20]))
                                self.add_cbindicator_inflation(2018,11,float(values[21]))
                                self.add_cbindicator_inflation(2018,12,float(values[22]))
                            elif(Worksheet.attrib['{urn:schemas-microsoft-com:office:spreadsheet}Name']=='Commercial actions'):
                                try:
                                    self.cbindicator_data
                                except NameError:
                                    self.cbindicator_data = CBIndicatorData.objects.all()
                                self.add_cbindicator_actions(2017,8 ,float(values[6]))
                                self.add_cbindicator_actions(2017,9 ,float(values[7]))
                                self.add_cbindicator_actions(2017,10,float(values[8]))
                                self.add_cbindicator_actions(2017,11,float(values[9]))
                                self.add_cbindicator_actions(2017,12,float(values[10]))
                                self.add_cbindicator_actions(2018,1 ,float(values[11]))
                                self.add_cbindicator_actions(2018,2 ,float(values[12]))
                                self.add_cbindicator_actions(2018,3 ,float(values[13]))
                                self.add_cbindicator_actions(2018,4 ,float(values[14]))
                                self.add_cbindicator_actions(2018,5 ,float(values[15]))
                                self.add_cbindicator_actions(2018,6 ,float(values[16]))
                                self.add_cbindicator_actions(2018,7 ,float(values[17]))
                                self.add_cbindicator_actions(2018,8 ,float(values[18]))
                                self.add_cbindicator_actions(2018,9 ,float(values[19]))
                                self.add_cbindicator_actions(2018,10,float(values[20]))
                                self.add_cbindicator_actions(2018,11,float(values[21]))
                                self.add_cbindicator_actions(2018,12,float(values[22]))
