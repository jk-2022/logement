from django.urls import path
from .views import LogementListView, LogementDetailView

urlpatterns = [
    path('', LogementListView.as_view(), name='logement-list'),
    path('<int:id>/', LogementDetailView.as_view(), name='logement-detail'),
]
