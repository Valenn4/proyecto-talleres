from django.urls import path
from .views import CategoryViewSet, MatchViewSet, NewViewSet, PositionLigaProfesionalViewSet
urlpatterns = [
    path("v1/categories", CategoryViewSet.as_view()),
    path("v1/news", NewViewSet.as_view()),
    path("v1/matches", MatchViewSet.as_view()),
    path("v1/positions/liga_profesional", PositionLigaProfesionalViewSet.as_view())
]