from django.contrib import admin
from django import forms
from django.contrib.postgres.forms import SimpleArrayField
from .models import Movie


class MovieAdminForm(forms.ModelForm):
    actors = SimpleArrayField(
        forms.CharField(max_length=200),
        delimiter=',',
        required=False,
        help_text="Enter actors separated by commas"
    )

    genre = SimpleArrayField(
        forms.CharField(max_length=200),
        delimiter=',',
        required=False,
        help_text="Enter genres separated by commas"
    )

    class Meta:
        model = Movie
        fields = "__all__"

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    form = MovieAdminForm
    list_display = ('name', 'director', 'year', 'language')
