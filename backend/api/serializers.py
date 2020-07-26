from rest_framework import serializers
from backend.api.models import Individual, Medication, MedicationType, Field, Species


class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ['pk', 'animal', 'species']


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ['pk', 'name', 'holding_number', 'id_number', 'gender', 'date_of_birth',
                  'mother', 'father', 'species']


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'


class MedicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationType
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
