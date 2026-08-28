from datetime import date

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"

class Address(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.city}, {self.street}"

    # To fix the Addre(sss) in admin panel
    class Meta:
        verbose_name_plural = "Address Entries"


class BookAuthor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.OneToOneField(
           Address, on_delete=models.CASCADE, null=True)

    def full_name(self):
         return f"{self.last_name}, {self.first_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    is_bestselling = models.BooleanField(default=False)
    last_update = models.DateField(auto_now=True, null=True)
    author = models.ForeignKey(BookAuthor, on_delete=models.CASCADE, null=True, related_name="books")
    published_countries = models.ManyToManyField(Country)

    def __str__(self):
        return f"{self.title!r} ({self.rating!r}) rev: {self.last_update}"
