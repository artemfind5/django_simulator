from django.db import models

# Create your models here.

class act_type(models.Model):
    id = models.IntegerField(primary_key=True)
    type = models.TextField()


# TODO: class acts - date type order_numb order_date