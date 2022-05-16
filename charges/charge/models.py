from django.db import models


# Create your models here.



class Charges(models.Model):
    price = models.IntegerField()
    cat = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)


class Category(models.Model):
    name = models.CharField(max_length=255)
    # food = models.IntegerField(null=True, blank=True,default=0)
    # clothes = models.IntegerField(null=True, blank=True, default=0)
    # car = models.IntegerField(null=True, blank=True,default=0)
    # flat = models.IntegerField(null=True, blank=True, default=0)
    # sum = models.IntegerField(null=True, blank=True,default=0)
    # data = models.DateTimeField(auto_now_add=True)



