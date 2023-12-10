from django.db import models

# Create your models here.

class Musician(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNo = models.CharField(max_length=12)
    InstrumentType = models.CharField(max_length=50)


    def __str__(self):
        return self.firstName
