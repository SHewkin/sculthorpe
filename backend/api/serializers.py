from rest_framework import serializers
from backend.api.models import Individual, Treatment, MedicationType, Field, Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['pk', 'species', 'breed']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['species'] = instance.get_species_display()

        return representation


class IndividualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Individual
        fields = ['pk', 'name', 'holding_number', 'id_number', 'gender', 'date_of_birth',
                  'mother', 'father', 'breed']

    def to_representation(self, instance):
        representation= super().to_representation(instance)
        representation['gender'] = instance.get_gender_display()

        return representation



class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        fields = '__all__'


class MedicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicationType
        fields = '__all__'


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'
