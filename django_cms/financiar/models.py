from django.db import models
from django.contrib.auth.models import User

class Channel(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='channels')
    
    def __str__(self):
            return self.name
        
class Brand(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='brands')
    
    def __str__(self):
            return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='categories')
    
    def __str__(self):
            return self.name
        
class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='subcategories')
    
    def __str__(self):
            return self.name
        
class Benchmark(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='benchmark')
    
    def __str__(self):
            return self.name
        
class ConstNetwork(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='const_networks')
    
    def __str__(self):
            return self.name
        
class SalesConcept(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='sales_concepts')
    
    def __str__(self):
            return self.name
        
class SalesConceptSize(models.Model):
    name = models.CharField(max_length=100)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='sales_conceptsize')
    
    def __str__(self):
            return self.name
        
class Location(models.Model):
    name = models.CharField(max_length=5)
    number = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=100, default=' ')
    channel = models.ForeignKey(Channel, null=True, on_delete=models.SET_NULL, related_name='locations')
    brand = models.ForeignKey(Brand, null=True, on_delete=models.SET_NULL, related_name='locations')
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, related_name='locations')
    subcategory = models.ForeignKey(Subcategory, null=True, on_delete=models.SET_NULL, related_name='locations')
    ebenchmark = models.ForeignKey(Benchmark, null=True, on_delete=models.SET_NULL, related_name='locations_E')
    bbenchmark = models.ForeignKey(Benchmark, null=True, on_delete=models.SET_NULL, related_name='locations_B')
    sales_concept = models.ForeignKey(SalesConcept, null=True, on_delete=models.SET_NULL, related_name='locations')
    sales_concept_size = models.ForeignKey(SalesConceptSize, null=True, on_delete=models.SET_NULL, related_name='locations')
    cn_vs_H = models.ForeignKey(ConstNetwork, null=True, on_delete=models.SET_NULL, related_name='locations_vsH')
    cn_vs_B = models.ForeignKey(ConstNetwork, null=True, on_delete=models.SET_NULL, related_name='locations_vsB')
    opened_from = models.DateField(default='2016-01-01')
    opened_to = models.DateField(default='2019-12-01')
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='locations')
    
    def __str__(self):
            return self.name.zfill(3) + " - " + self.title

class Lookup(models.Model):
    name = models.CharField(max_length=100)

class LocationFull(models.Model):
    name = models.CharField(max_length=5)
    number = models.PositiveSmallIntegerField(default=1)
    title = models.CharField(max_length=100, default=' ')
    channel =models.CharField(max_length=100, default=' ')
    brand = models.CharField(max_length=100, default=' ')
    category = models.CharField(max_length=100, default=' ')
    subcategory =models.CharField(max_length=100, default=' ')
    ebenchmark = models.CharField(max_length=100, default=' ')
    bbenchmark = models.CharField(max_length=100, default=' ')
    sales_concept = models.CharField(max_length=100, default=' ')
    sales_concept_size = models.CharField(max_length=100, default=' ')
    cn_vs_H = models.CharField(max_length=100, default=' ')
    cn_vs_B = models.CharField(max_length=100, default=' ')
    opened_from = models.DateField(default='2016-01-01')
    opened_to = models.DateField(default='2019-12-01')
    
    def __str__(self):
            return self.name.zfill(3) + " - " + self.title
        
class LocationFinal(models.Model):
    number = models.PositiveIntegerField(default=1)
    title = models.CharField(max_length=100, default=' ')
    year = models.PositiveSmallIntegerField(default=2017)
    month = models.PositiveSmallIntegerField(default=1)
    base = models.FloatField(default = 0)
    trend = models.FloatField(default = 0)
    infla = models.FloatField(default = 0)
    actions = models.FloatField(default = 0)
    matur = models.FloatField(default = 0)
    traffic = models.FloatField(default = 0)
        
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

    location = models.ForeignKey(Location, related_name='sales_data', on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField(default=2017)
    month = models.PositiveSmallIntegerField(default=1)
    open = models.BooleanField(default = True)
    matur = models.FloatField(default = 0)
    value = models.FloatField(default = 0)
    traffic = models.FloatField(default = 0)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='sales_data')
    type = models.PositiveIntegerField(choices = DATA_TYPE, default=0)
        
    class Meta:
        index_together = ["location", "year", "month"]
#             indexes = [
#                 models.Index(fields=['first_name'], name='first_name_idx'),
#             ]        

class ChannelBrandIndicator(models.Model):
    name = models.CharField(max_length=100)
    bbenchmark = models.BooleanField(default = 0)
    ebenchmarks = models.ManyToManyField(Benchmark, blank=True)
    bchannel = models.BooleanField(default = 0)
    channels = models.ManyToManyField(Channel, blank=True)
    bbrand =  models.BooleanField(default = 0)
    brands = models.ManyToManyField(Brand, blank=True)
    bcategory =  models.BooleanField(default = 0)
    categories = models.ManyToManyField(Category, blank=True)
    bsubcategory =  models.BooleanField(default = 0)
    subcategories = models.ManyToManyField(Subcategory, blank=True)
    bsalesconcept =  models.BooleanField(default = 0)
    salesconcepts = models.ManyToManyField(SalesConcept, blank=True)
    bsalesconceptsize =  models.BooleanField(default = 0)
    salesconceptsizes = models.ManyToManyField(SalesConceptSize, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='cbindicators')
    
    def __str__(self):
            return self.name
    
class CBIndicatorData(models.Model):
    indicator = models.ForeignKey(ChannelBrandIndicator, related_name='indicator_data', on_delete=models.CASCADE)
    year = models.PositiveSmallIntegerField(default=2017)
    month = models.PositiveSmallIntegerField(default=1)
    trend = models.FloatField(default = 0)
    inflation = models.FloatField(default = 0)
    commercial_actions = models.FloatField(default = 0)
    updated = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, related_name='cbindicatordata')
    
class GraficData(models.Model):
    year = models.PositiveSmallIntegerField(default=2017)
    month = models.PositiveSmallIntegerField(default=1)
    base = models.FloatField(default = 0)
    trend = models.FloatField(default = 0)
    inflation = models.FloatField(default = 0)
    commercial_actions = models.FloatField(default = 0)
    matur = models.FloatField(default = 0)
    traffic = models.FloatField(default = 0)
    fullx = models.FloatField(default = 0)
