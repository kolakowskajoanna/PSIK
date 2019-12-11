from abc import ABC

from rest_framework import serializers
from schronisko.schroniskoo.models import *


class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = 'pojemnosc'


class PiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pies
        fields = ('imie','rasa','wiek', 'plec','wielkosc', 'umaszczenie', 'znaki_szczegolne','stan_zdrowia',
                  'usposobienie','box')


class AdopterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopter
        fields = ('imie','nazwisko','numer_tel','adres','dzieci')


class AdopcjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adopcja
        fields = ('pies','adopter','data','status')

