from django import forms
from .models import Products

class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['id', 'productName', 'supplierID', 'categoryID', 'quantityPerUnit', 'unitPrice', 'unitsInStock', 'unitsOnOrder', 'reorderLevel', 'discontinued']
