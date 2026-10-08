"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""
from rest_framework import viewsets  # noqa: F401  (a utiliser)

from .models import Reservation, Salle  # noqa: F401  (a utiliser)

# TODO : votre code ici

# TACHES 3

from .serializers import ReservationSerializer , SalleSerializer

from .models import Reservation, Salle


class SalleViewSet(viewsets.ModelViewSet): # GRACE AU VIEWSET on pourra manipuler les instances comme avec un crud
    serializer_class = SalleSerializer

    def get_queryset(self):
            # On conserve nos optimisations des exercices précédents
            queryset = Salle.objects.select_related().all()
               
            return queryset


class RservationViewSet(viewsets.ModelViewSet): # GRACE AU VIEWSET on pourra manipuler les instances comme avec un crud
    serializer_class = ReservationSerializer

    def get_queryset(self):
        # On conserve nos optimisations des exercices précédents
        queryset = Reservation.objects.select_related().all()
           
        return queryset

    def perform_create(self, serializer):
        # On conserve l'attribution automatique de l'utilisateur
        serializer.save(ajoute_par=self.request.user)