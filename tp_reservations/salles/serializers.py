"""Tache 1 et 2 : serializers et validation.

A FAIRE :
  - SalleSerializer (ModelSerializer)
  - ReservationSerializer (ModelSerializer) :
      * le champ `utilisateur` est en LECTURE SEULE (il sera renseigne par la vue)
      * validation : `fin` strictement apres `debut`
      * validation : pas de chevauchement avec une autre reservation CONFIRMEE
        de la meme salle
"""
from rest_framework import serializers

from .models import Reservation, Salle  # noqa: F401  (a utiliser)

# TODO : votre code ici

# LE TP DE DJANGO EN SALLE 

#TACHE 1
from salles.models import Salle, Reservation

# CREONS NONS SERIALIAZER
class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ['nom', 'capacite', 'batiment']  # Liste explicite des champs  
        

class  ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['Statut', 'salle','utilisateur','debut','fin', 'motif', 'cree_le']  # Liste explicite des champs 
        read_only_fields = ['utilisateur']


    def validate(self, attrs):
        
        if attrs['fin'] < attrs['debut']: # attrs pour le nom global attributes un dictionnaire de DRF on peut aussi utiliser data, pour 
            #avoir tout les champs et dans ce tout on choisit de traiter ['date_retour_prevue'] < attrs['date_emprunt']
            raise serializers.ValidationError(
                "La date de retour prévue ne peut pas être antérieure à la date d'emprunt."
            )
        return attrs