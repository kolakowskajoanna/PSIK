# Generated by Django 2.2.7 on 2019-11-14 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=30)),
                ('nazwisko', models.CharField(max_length=45)),
                ('numer_tel', models.CharField(max_length=9)),
                ('adres', models.CharField(max_length=150)),
                ('dzieci', models.BooleanField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pojemnosc', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=45)),
                ('rasa', models.CharField(max_length=45)),
                ('wiek', models.IntegerField()),
                ('plec', models.BooleanField()),
                ('wielkosc', models.CharField(max_length=10)),
                ('umaszczenie', models.CharField(max_length=60)),
                ('znaki_szczegolne', models.CharField(max_length=100)),
                ('stan_zdrowia', models.CharField(max_length=120)),
                ('usposobienie', models.CharField(max_length=150)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schroniskoo.Box')),
            ],
        ),
        migrations.CreateModel(
            name='Adopcja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('status', models.BooleanField(default=1)),
                ('adopter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schroniskoo.Adopter')),
                ('pies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schroniskoo.Pies')),
            ],
        ),
    ]
