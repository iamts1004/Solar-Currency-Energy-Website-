from django.db import models

class Energy_Table(models.Model):
    Name = models.CharField(max_length=50)
    Phone = models.IntegerField()
    Address = models.CharField(max_length=200)
    Energy = models.IntegerField()
    SolarEcoins = models.IntegerField()




