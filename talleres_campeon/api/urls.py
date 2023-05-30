from django.urls import path
from .views import CategoryViewSet, NewViewSet
urlpatterns = [
    path("v1/categories", CategoryViewSet.as_view()),
    path("v1/news", NewViewSet.as_view())
]