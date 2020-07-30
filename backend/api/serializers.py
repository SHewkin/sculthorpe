from rest_framework import serializers
from backend.api.models import Individual, Treatment, MedicationType, Field, Breed, Note


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['pk', 'species', 'breed']

class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ['pk', 'name', 'holding_number', 'id_number', 'gender', 'date_of_birth',
                  'mother', 'father', 'breed', 'field']


class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = ['pk', 'medication_type', 'amount_administered', 'date_of_administration',
                  'individual']


class MedicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationType
        fields = ['pk', 'name', 'description']


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = ['pk', 'name', 'description']


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['pk', 'note', 'individual']
