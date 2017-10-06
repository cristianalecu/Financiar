from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class Channel(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class Brand(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class Benchmark(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class ConstNetwork(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class SalesConcept(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class SalesConceptSize(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
            return self.name
        
class SalesData(models.Model):
    DATA_TYPE = (
    (0,'Sales value'),
    (10,'Simulate'),
    (20,'ProjectedLvl1'),
    (21,'ProjectedLvl2'),
    (22,'ProjectedLvl3'),
    (30,'ToBeDeleted'),
    (40,'Other'),
    )

    location = models.ForeignKey(Location, related_name='sales_data')
    channel = models.ForeignKey(Channel, related_name='sales_data')
    brand = models.ForeignKey(Brand, related_name='sales_data')
    category = models.ForeignKey(Category, related_name='sales_data')
    subcategory = models.ForeignKey(Subcategory, related_name='sales_data')
    ebenchmark = models.ForeignKey(Benchmark, related_name='sales_data_E')
    bbenchmark = models.ForeignKey(Benchmark, related_name='sales_data_B')
    sales_concept = models.ForeignKey(SalesConcept, related_name='sales_data')
    sales_concept_size = models.ForeignKey(SalesConceptSize, related_name='sales_data')
    cn_vs_H = models.ForeignKey(ConstNetwork, related_name='sales_data_vsH')
    cn_vs_B = models.ForeignKey(ConstNetwork, related_name='sales_data_vsB')
    year = models.PositiveSmallIntegerField(default=2017)
    month = models.PositiveSmallIntegerField(default=1)
    project = models.BooleanField(default = True)
    open = models.BooleanField(default = True)
    value = models.FloatField(default = 0)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='sales_data')
    type = models.PositiveIntegerField(choices = DATA_TYPE, default=0)

    def __str__(self):
            return self.location + '_' + self.year + '_' + self.month 