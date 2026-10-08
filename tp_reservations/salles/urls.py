"""Tache 3 : brancher les ViewSets sur un DefaultRouter.

Les routes attendues sont (prefixe /api/ deja fourni par config/urls.py) :
  /api/salles/            /api/salles/{id}/
  /api/reservations/      /api/reservations/{id}/
  /api/salles/{id}/occupation/
"""

#taches 3
from rest_framework.routers import DefaultRouter 
from .views import RservationViewSet, SalleViewSet
from django.urls import path, include




#TACHES 3 LE ROUTER 
# 1. On instancie le router
router = DefaultRouter()

# 2. On enregistre notre ViewSet auprès du router

router.register('Salles', SalleViewSet, basename='salles')
router.register('Reservations', RservationViewSet, basename='Reservation')


urlpatterns = [
    # 3. On inclut toutes les URLs générées automatiquement par le router
    path('', include(router.urls)),
]
