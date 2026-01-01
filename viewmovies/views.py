from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg
from .models import Movie, Ratings
from .forms import RatingsForm, RegisterForm


# Create your views here.

def view_movie_names(request):
    movies = Movie.objects.all()
    return render(request, 'viewmovies/index.html', {'movies': movies})


def get_movie_info(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    user_rating = None
    if request.user.is_authenticated:
        user_rating = Ratings.objects.filter(
            user=request.user,
            movie=movie
        ).first()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect("login")

        form = RatingsForm(request.POST)
        if form.is_valid():
            rating_value = form.cleaned_data["rating"]

            Ratings.objects.update_or_create(
                user=request.user,
                movie=movie,
                defaults={"rating": rating_value},
            )

            messages.success(request, "Your rating has been saved.")
            return redirect("movie_details", movie_id=movie.id)
    else:
        form = RatingsForm(instance=user_rating)

    avg_rating = Ratings.objects.filter(movie=movie).aggregate(
        avg=Avg("rating")
    )["avg"]

    return render(request, "viewmovies/movie_details.html", {
        "movie": movie,
        "form": form,
        "user_rating": user_rating,
        "avg_rating": avg_rating,
    })
    
    
""" for new user registration """
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # name of login URL
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form": form})