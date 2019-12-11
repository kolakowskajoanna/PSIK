from django.db import models


# Create your models here.
class Box(models.Model):
    pojemnosc= models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='boxs', on_delete=models.CASCADE)


class Pies(models.Model):
    imie=models.CharField(max_length=45)
    rasa=models.CharField(max_length=45)
    wiek=models.IntegerField()
    plec=models.BooleanField()
    wielkosc=models.CharField(max_length=10)
    umaszczenie=models.CharField(max_length=60)
    znaki_szczegolne=models.CharField(max_length=100)
    stan_zdrowia=models.CharField(max_length=120)
    usposobienie=models.CharField(max_length=150)
    box=models.ForeignKey(Box, on_delete=models.CASCADE)
    owner= models.ForeignKey('auth.User', related_name='piess', on_delete=models.CASCADE)


class Adopter(models.Model):
    imie=models.CharField(max_length=30)
    nazwisko=models.CharField(max_length=45)
    numer_tel=models.CharField(max_length=9)
    adres=models.CharField(max_length=150)
    dzieci=models.BooleanField(default=0)
    owner = models.ForeignKey('auth.User', related_name='adopters', on_delete=models.CASCADE)


class Adopcja(models.Model):
    pies=models.ForeignKey(Pies, on_delete=models.CASCADE)
    adopter=models.ForeignKey(Adopter, on_delete=models.CASCADE)
    data=models.DateField()
    status=models.BooleanField(default=1)
    owner = models.ForeignKey('auth.User', related_name='adopcjas', on_delete=models.CASCADE)
