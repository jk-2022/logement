from django.db import models
from users.models import User

class Logement(models.Model):
    TYPE_CHOICES = [
        ('location', 'Location'),
        ('vente', 'Vente')
    ]
    STATUT_CHOICES = [
        ('disponible', 'Disponible'),
        ('en_conversation', 'En conversation'),
        ('vendu_loue', 'Vendu/Loué'),
    ]

    demarcheur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='logements')
    titre = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    adresse = models.CharField(max_length=255)
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='disponible')
    date_publication = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.titre} - {self.statut}"
