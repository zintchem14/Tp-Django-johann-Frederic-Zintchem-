"""Tache 4 : permissions personnalisees.

A FAIRE :
  - IsOwnerOrReadOnly : lecture pour tous, modification/suppression
    reservee a l'auteur de la reservation (obj.utilisateur).
"""
#taches 4

from rest_framework import permissions  # noqa: F401  (a utiliser)

# TODO : votre code ici



class IIsOwnerOrReadOnly (permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        # 1. Si la méthode est SAFE (GET, HEAD, OPTIONS), on autorise la lecture
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return hasattr(obj.reservations, 'utilisateur') and obj.reservations.utilisateur == request.utilisateur  
