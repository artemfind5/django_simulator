from django.db import models

# Create your models here.

class act_type(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.TextField()

class acts(models.Model):
    act_date = models.DateField()
    act_type = models.TextField()
    order_numb = models.IntegerField()
    order_date = models.DateField()
    file_path = models.FileField()

# TODO: class acts - date type order_numb order_date