from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    biography = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
