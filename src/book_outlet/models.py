from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=50)
  rating = models.IntegerField()

  def __str__(self):
      return f"{self.title!r} ({self.rating!r})"
