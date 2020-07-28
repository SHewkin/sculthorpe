from django.db import models
from rest_framework import serializers


class Breed(models.Model):
    SPECIES_CHOICES = (
        ('S', 'Sheep'),
        ('C', 'Cow')
    )
    species = models.CharField(max_length=100, choices=SPECIES_CHOICES)
    breed = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.species}: {self.breed}"


class Individual(models.Model):
    GENDER_OPTIONS = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=100)
    holding_number = models.CharField(max_length=50)
    id_number = models.CharField(max_length=50)
    gender = models.CharField(max_length=100, choices=GENDER_OPTIONS)
    date_of_birth = models.DateField()
    mother = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE,
        limit_choices_to={"gender":"F"}, related_name="+")
    father = models.ForeignKey(
        'self', null=True, blank=True, on_delete=models.CASCADE,
        limit_choices_to={"gender":"M"}, related_name="+")
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class MedicationType(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()


class Treatment(models.Model):
    medication_type = models.ForeignKey(
        MedicationType, on_delete=models.CASCADE)
    amount_administered = models.FloatField()
    date_of_administration = models.DateField()
    individual = models.ForeignKey(Individual, on_delete=models.CASCADE)


class Field(models.Model):
    name = models.CharField(max_length=100)
    individuals = models.ManyToManyField(Individual)
