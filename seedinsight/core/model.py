from django.db import models

class Ecozone(models.Model):
    name = models.CharField(max_length=100)
    altitude = models.FloatField()
    temperature = models.FloatField()
    rainfall = models.FloatField()
    soil_type = models.CharField(max_length=100)
    attributes = models.TextField()

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100, choices=[('Seeds', 'Seeds'), ('Chemicals', 'Chemicals'), ('Fertilizers', 'Fertilizers')])

    def __str__(self):
        return self.name

class Seed(models.Model):
    name = models.CharField(max_length=100)
    ecozone = models.ForeignKey(Ecozone, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    seed_rate = models.FloatField()
    maturity_period = models.IntegerField()
    yield_per_acre = models.FloatField()
    attributes = models.TextField()

    def __str__(self):
        return self.name

