from django.urls import path
from .views import (
    LogementListView, LogementDetailView, LogementCreateView,
    LogementDashboardView, LogementUpdateView, LogementDesactiverView
)

urlpatterns = [
    path('', LogementListView.as_view(), name='logement-list'),
    path('<int:id>/', LogementDetailView.as_view(), name='logement-detail'),
    path('create/', LogementCreateView.as_view(), name='logement-create'),
    path('dashboard/', LogementDashboardView.as_view(), name='logement-dashboard'),
    path('<int:pk>/update/', LogementUpdateView.as_view(), name='logement-update'),
    path('<int:pk>/desactiver/', LogementDesactiverView.as_view(), name='logement-desactiver'),
]
