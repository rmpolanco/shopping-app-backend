from django.db import models

# Create your models here.

class Item(models.Model):
    product_name = models.CharField(max_length = 100)
    company_name = models.CharField(max_length = 100)
    reg_price = models.DecimalField(decimal_places = 2, max_digits=15)
    sale_price = models.DecimalField(decimal_places = 2, max_digits=15)
    category = models.CharField(max_length = 100)
    on_sale = models.BooleanField(default = False)

    def __str__(self):
        return self.product_name
    
