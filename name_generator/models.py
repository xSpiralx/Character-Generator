from django.db import models

# Create your models here.
from django.db import models

class Character(models.Model):
    race = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    character_class = models.CharField(max_length=100)
    generated_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.race} {self.gender} {self.character_class}"
