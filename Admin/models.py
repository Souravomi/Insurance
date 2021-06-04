from django.db import models

# Create your models here.


class Policies(models.Model):
    Policy = models.CharField(max_length=10,null=True)
    Category = models.CharField(max_length=10)
    Scheme = models.CharField(max_length=10)
    Scheme_Amount = models.CharField(max_length=10)
    Maturity_Amount = models.CharField(max_length=20)
    Maturity_Period = models.CharField(max_length=10)