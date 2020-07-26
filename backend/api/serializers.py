from rest_framework import serializers
from api.models import Individual, Medication, MedicationType, Field, Species

class SpeciesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Species
        fields='__all__'


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model=Individual
        fields='__all__'


class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medication
        fields='__all__'


class MedicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model=MedicationType
        fields='__all__'



class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model=Field
        fields='__all__'


