from django.db import models


class Director(models.Model):
    name = models.TextField(max_length=20)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    duration = models.BooleanField(default=True)



    def __str__(self):
        return self.title


class Review(models.Model):
    text = models.TextField(max_length=200)
