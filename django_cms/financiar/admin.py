from django.contrib import admin

from financiar import models as finmodels

admin.site.register(finmodels.Channel)
admin.site.register(finmodels.Brand)
admin.site.register(finmodels.Category)
admin.site.register(finmodels.Subcategory)
admin.site.register(finmodels.Benchmark)
admin.site.register(finmodels.SalesConcept)
admin.site.register(finmodels.SalesConceptSize)
admin.site.register(finmodels.Location)

admin.site.register(finmodels.SalesData)

