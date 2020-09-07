from django.db import models

# Create your models here.


class Retails(models.Model):
    name = models.CharField(max_length=100)
    min_qualification = models.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_absolute_url(self):
        return "Retail/{0}".format(self.id)


class Consumer(models.Model):
    name = models.CharField(max_length=100)


