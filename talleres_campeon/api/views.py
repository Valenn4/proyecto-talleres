from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category, New, Match, PositionLigaProfesional
from .serializer import NewSerializer, CategorySerializer, MatchSerializer, PositionLigaProfesionalSerializer

# Create your views here.


class CategoryViewSet(APIView):
    def get(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = CategorySerializer(data=request.data, many=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NewViewSet(APIView):
    def get(self, request):
        queryset = New.objects.all()
        serializer = NewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = NewSerializer(data=request.data, many=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MatchViewSet(APIView):
    def get(self, request):
        model = Match.objects.all()
        serializer = MatchSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = MatchSerializer(data=request.data, many=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PositionLigaProfesionalViewSet(APIView):
    def get(self, request):
        model = PositionLigaProfesional.objects.all()
        serializer = PositionLigaProfesionalSerializer(model, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = PositionLigaProfesionalSerializer(data=request.data, many=True)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)