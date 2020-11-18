from django.contrib.auth.models import User
from django.db import models

class Products(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    code = models.IntegerField()
    active = models.BooleanField(default=True)
    quantity_in_stock = models.IntegerField()
    #seller = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    def __str__(self):
        return self.title

   
