from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSeriliazer
from .models import Room

# Create your views here.


class RoomView(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSeriliazer
