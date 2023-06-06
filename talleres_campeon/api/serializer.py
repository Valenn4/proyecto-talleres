from .models import New, Category, Match, PositionLigaProfesional
from rest_framework import serializers

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ["title", "description", "other_description", "image", "category"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]

class MatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields = '__all__'

class PositionLigaProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionLigaProfesional
        fields = '__all__'

