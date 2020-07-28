from django.contrib import admin

from backend.api.models import Individual, Treatment, MedicationType, Breed, Field

admin.site.register(Breed)
admin.site.register(Individual)
admin.site.register(MedicationType)
admin.site.register(Treatment)
admin.site.register(Field)
