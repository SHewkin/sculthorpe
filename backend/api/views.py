from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework import viewsets

from .models import Field, Individual, Treatment, MedicationType, Breed
from .serializers import (FieldSerializer, IndividualSerializer,
                          TreatmentSerializer, MedicationTypeSerializer,
                          BreedSerializer)

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class IndividualViewSet(viewsets.ModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer


class TreatmentViewSet(viewsets.ModelViewSet):
    queryset = Treatment.objects.all()
    serializer_class = TreatmentSerializer


class MedicationTypeViewSet(viewsets.ModelViewSet):
    queryset = MedicationType.objects.all()
    serializer_class = MedicationTypeSerializer


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
