from django.contrib.auth.models import User
from rest_framework import serializers
from schronisko.schroniskoo.models import *


class BoxSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyFiled(source='owner.username')

    class Meta:
        model = Box
        fields = ['pojemnosc', 'owner']


class PiesSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyFiled(source='owner.username')

    class Meta:
        model = Pies
        fields = ['imie','rasa','wiek', 'plec','wielkosc', 'umaszczenie', 'znaki_szczegolne','stan_zdrowia',
                  'usposobienie','box', 'owner']


class AdopterSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyFiled(source='owner.username')

    class Meta:
        model = Adopter
        fields = ['imie','nazwisko','numer_tel','adres','dzieci', 'owner']


class AdopcjaSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyFiled(source='owner.username')

    class Meta:
        model = Adopcja
        fields = ['pies','adopter','data','status', 'owner']


class UserSerializer(serializers.ModelSerializer):
     questions = serializers.PrimaryKeyRelatedFiled(many=True, queryset=Pies.objects.all())

     class Meta:
         model = User
         fields = ['id', 'username', 'questions']