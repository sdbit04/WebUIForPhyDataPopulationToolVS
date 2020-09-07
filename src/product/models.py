from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=100)
    # For this class I am creating a table having two fields, and data type of the two columns is models.TextField
    # a row will be added into the table while a new object will be created.
