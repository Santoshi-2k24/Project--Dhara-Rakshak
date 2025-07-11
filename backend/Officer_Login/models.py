import random
from django.db import models
from django.core.validators import MinLengthValidator

def generate_officer_id():
    return str(random.randint(10**6, 10**9 - 1))  # generates 7-9 digit unique id

class Officer(models.Model):
    id = models.CharField(primary_key=True, default=generate_officer_id, unique=True, max_length=10, editable=False)
    name = models.CharField(max_length=200)
    password = models.CharField(max_length=200, validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.name
