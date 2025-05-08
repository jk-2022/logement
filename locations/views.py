from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Logement
from .serializers import LogementSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

class LogementListView(generics.ListAPIView):
    queryset = Logement.objects.filter(statut='disponible')
    serializer_class = LogementSerializer

class LogementDetailView(generics.RetrieveAPIView):
    queryset = Logement.objects.all()
    serializer_class = LogementSerializer
    lookup_field = 'id'

class LogementCreateView(generics.CreateAPIView):
    queryset = Logement.objects.all()
    serializer_class = LogementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(demarcheur=self.request.user)

class LogementDashboardView(generics.ListAPIView):
    serializer_class = LogementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Logement.objects.filter(demarcheur=self.request.user)
    
class LogementUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = LogementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Logement.objects.filter(demarcheur=self.request.user)

class LogementDesactiverView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            logement = Logement.objects.get(pk=pk, demarcheur=request.user)
            logement.statut = 'indisponible'
            logement.save()
            return Response({'message': 'Logement désactivé'}, status=status.HTTP_200_OK)
        except Logement.DoesNotExist:
            return Response({'error': 'Logement introuvable'}, status=status.HTTP_404_NOT_FOUND)