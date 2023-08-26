from django.shortcuts import render
from rest_framework import viewsets
from .serilization import Movieserializer
from .models import movie



# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):
    queryset = movie.objects.all()
    serializer_class = Movieserializer