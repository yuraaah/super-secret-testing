from dataclasses import field
from pyexpat import model
from statistics import mode
from rest_framework import serializers
from .models import Room


class RoomSeriliazer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_edit',
                  'mark_to_delete', 'created_at')
