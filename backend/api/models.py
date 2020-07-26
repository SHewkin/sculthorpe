from django.db import models
from rest_framework import serializers



class Species(models.Model):
    ANIMAL_CHOICES = (
        ('S', 'Sheep'),
        ('C', 'Cow')
    )
    animal = models.CharField(max_length=100, choices=ANIMAL_CHOICES)
    species = models.CharField(max_length=100)


class Individual(models.Model):
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=100)
    holding_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=100, choices=GENDER_OPTIONS)
    id_number = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    parent = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class MedicationType(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()


class Medication(models.Model):
    medication_type = models.ForeignKey(
        MedicationType, on_delete=models.CASCADE)
    amount_administered = models.FloatField()
    date_of_administration = models.DateField()
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)

class Field(models.Model):
    name = models.CharField(max_length = 100)
    individuals = models.ManyToManyField(Individual)