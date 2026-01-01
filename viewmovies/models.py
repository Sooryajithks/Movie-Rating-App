from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.core.validators import MaxValueValidator

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=200)
    synopsis = models.CharField(max_length=800)
    director = models.CharField(max_length=200)
    actors = ArrayField(models.CharField(max_length=600),       
                        blank=True, default=list)
    poster = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    genre = ArrayField(models.CharField(max_length=200),
                       blank=True, default=list)
    year = models.PositiveSmallIntegerField()
    
    
    def __str__(self):
        return self.name
    
class Ratings(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"],
                name="one_rating_per_user_per_movie"
            )
        ]

