from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=1000, decimal_places=2)
    creation_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(
        'Category', #The name of the model
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

