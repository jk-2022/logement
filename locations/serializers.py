from rest_framework import serializers
from .models import Logement

class LogementSerializer(serializers.ModelSerializer):
    demarcheur = serializers.ReadOnlyField(source='demarcheur.username')

    class Meta:
        model = Logement
        fields = [
            'id', 'titre', 'description', 'prix', 'type', 'adresse',
            'statut', 'date_publication', 'demarcheur'
        ]

