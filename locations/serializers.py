from rest_framework import serializers
from .models import Logement
from users.serializers import UserSerializer

class LogementSerializer(serializers.ModelSerializer):
    demarcheur = UserSerializer(read_only=True)

    class Meta:
        model = Logement
        fields = [
            'id', 'titre', 'description', 'prix', 'type', 'adresse',
            'statut', 'date_publication', 'demarcheur'
        ]
