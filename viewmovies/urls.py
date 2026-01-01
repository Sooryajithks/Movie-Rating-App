from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_movie_names, name='movielistpage'),
    path('register/', views.register, name="register"),
    path('<int:movie_id>/', views.get_movie_info, name='movie_details'),
]
