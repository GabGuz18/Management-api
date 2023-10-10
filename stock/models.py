from django.db import models

# Create your models here.
class Categories(models.Model):
    category=models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.category

class Products(models.Model):
    product = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product

class Ingredients(models.Model):
    ingredient = models.CharField(max_length=100, blank=False, null=False)
    quantity = models.IntegerField()
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.ingredient

class Sales(models.Model):
    table = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.table + ' ' + self.date

class Product_sales(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=3)
    #Money
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    sale = models.ForeignKey(Sales, on_delete=models.CASCADE)

class Purchases(models.Model):
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.date

class Product_purchases(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    purchase = models.ForeignKey(Purchases, on_delete=models.CASCADE)