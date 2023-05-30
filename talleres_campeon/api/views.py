from django.shortcuts import render
from rest_framework import generics, mixins
from .models import Category, New
from .serializer import NewSerializer, CategorySerializer

# Create your views here.


class CategoryViewSet(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class NewViewSet(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = New.objects.all().order_by("-id")
    serializer_class = NewSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)