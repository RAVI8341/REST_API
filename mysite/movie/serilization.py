from rest_framework import serializers
from .models import movie

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        fields = ['id','name','duration','rating']