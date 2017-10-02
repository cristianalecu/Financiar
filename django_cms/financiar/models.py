from django.db import models

class SupplierOrder(models.Model):
    ORDER_STATUS = (
    (0,'Placed'),
    (1,'In process'),
    (1,'In delivery'),
    (3,'Delivered'),
    (4,'Paid'),
    (5,'Closed'),
    )

    user = models.ForeignKey(User, related_name='supplier_orders')
    customer = models.ForeignKey(Customer, related_name='supplier_orders')
    supplier = models.ForeignKey(Supplier, related_name='supplier_orders')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)    
    notes = models.CharField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.PositiveIntegerField(choices = ORDER_STATUS, default=0)
    
    def __str__(self):
            return 'Order {}'.format(self.id)