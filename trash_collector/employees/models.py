from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=5)
    user = models.ForeignKey('accounts.User', blank=True, null=True, on_delete=models.CASCADE)
# TODO: Create an Employee model with properties required by the user stories