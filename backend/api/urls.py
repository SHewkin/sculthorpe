from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'individual', views.IndividualViewSet)
router.register(r'treatment', views.TreatmentViewSet)
router.register(r'medication_type', views.MedicationTypeViewSet)
router.register(r'breed', views.BreedViewSet)
router.register(r'field', views.FieldViewSet)
router.register(r'note', views.NoteViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]