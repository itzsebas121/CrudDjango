from django.db import models

# Create your models here.
class Products(models.Model):
    id = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    supplierID = models.IntegerField()
    categoryID = models.IntegerField()
    quantityPerUnit = models.CharField(max_length=100)
    unitPrice = models.IntegerField()
    unitsInStock = models.IntegerField()
    unitsOnOrder = models.IntegerField()
    reorderLevel = models.IntegerField()
    discontinued = models.BooleanField()
    
    def __str__(self):
        return self.productName