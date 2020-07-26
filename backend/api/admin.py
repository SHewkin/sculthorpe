from django.contrib import admin

from api.models import Individual, Medication, MedicationType, Species, Field

admin.site.register(Species)
admin.site.register(Individual)
admin.site.register(MedicationType)
admin.site.register(Medication)
admin.site.register(Field)