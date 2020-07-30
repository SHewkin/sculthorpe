from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Breed, Field, Individual, MedicationType, Treatment, Note
from .serializers import (BreedSerializer, FieldSerializer,
                          IndividualSerializer, MedicationTypeSerializer,
                          TreatmentSerializer, NoteSerializer)

# Serve Vue Application
index_view = never_cache(TemplateView.as_view(template_name='index.html'))


class IndividualViewSet(viewsets.ModelViewSet):
    queryset = Individual.objects.all()
    serializer_class = IndividualSerializer

    @action(detail=True, methods=['get'])
    def treatments(self, request, pk=None):
        individual = Individual.objects.get(pk=pk)
        treatments = Treatment.objects.filter(individual=individual).order_by(
            '-date_of_administration')

        serializer = TreatmentSerializer(treatments, many=True)

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def notes(self, request, pk=None):
        individual = Individual.objects.get(pk=pk)
        notes = Note.objects.filter(individual=individual)

        serializer = NoteSerializer(notes, many=True)

        return Response(serializer.data)


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


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
