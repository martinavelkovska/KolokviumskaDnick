from django.contrib.auth.models import User
from django.db import models

# Create your models here.

TYPE_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
)

class Pilot(models.Model):
    ime = models.CharField(max_length=20)
    prezime = models.CharField(max_length=20)
    birth_year = models.IntegerField()
    casovi = models.IntegerField()
    role = models.CharField(max_length=20)

    def __str__(self):
        return self.ime+" "+self.prezime

class Balloon(models.Model):
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='1')
    proizvoditel = models.CharField(max_length=40)
    max_patnici = models.IntegerField()

    def __str__(self):
        return f"{self.type} - {self.proizvoditel}"

class Airline(models.Model):
    ime = models.CharField(max_length=35)
    year_created = models.IntegerField()
    europe = models.BooleanField()

    def __str__(self):
        return self.ime

class Flight(models.Model):
    sifra = models.CharField(max_length=20)
    aerodrom_From = models.CharField(max_length=35)
    aerodrom_To = models.CharField(max_length=35)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.FileField(upload_to="files/", null=True, blank=True)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.sifra)

class AirlinePilot(models.Model):
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pilot) + " - " + str(self.airline)
