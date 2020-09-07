from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=200)
    phone = models.IntegerField()


    def __str__(self):
        return self.name
    


