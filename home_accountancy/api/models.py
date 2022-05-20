from operator import truediv
from django.db import models
import string
import random


def generate_unique_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break

    return code

    # Create your models here.


class Room(models.Model):
    code = models.CharField(max_length=6, default="", unique=True)
    host = models.CharField(max_length=50, unique=True)
    guest_can_edit = models.BooleanField(null=False, default=False)
    mark_to_delete = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
