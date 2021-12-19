from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name + ' by ' + self.author