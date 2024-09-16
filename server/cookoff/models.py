import uuid
from django.db import models
from django.contrib.auth import get_user_model
from participant.models import Participant

User = get_user_model()

class CookOff(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    open = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

class Dish(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    cookoff = models.ForeignKey(CookOff, on_delete=models.CASCADE)

class Vote(models.Model):
    value = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    voter = models.ForeignKey(Participant, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['voter', 'dish'], name='One vote per participant')
        ]

