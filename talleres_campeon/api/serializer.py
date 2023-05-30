from .models import New, Category
from rest_framework import serializers

class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = ["title", "description", "other_description", "image", "category"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]