from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Logement
from .serializers import LogementSerializer

class LogementListView(generics.ListAPIView):
    queryset = Logement.objects.filter(statut='disponible')
    serializer_class = LogementSerializer

class LogementDetailView(generics.RetrieveAPIView):
    queryset = Logement.objects.all()
    serializer_class = LogementSerializer
    lookup_field = 'id'
