from django.urls import path
from . import views

app_name = "app"
urlpatterns = [
    # ex. /
    path("", views.index, name='index'),
    # ex. /login
    path("login", views.login_user, name='login'),
    # ex. /logout
    path("logout", views.logout_user, name='logout'),
    # ex. /register
    path("register", views.register, name='register'),
    # ex. /profile
    path("profile", views.profile, name='profile'),
    # ex. /pets
    path("pets", views.available_pets, name='pets'),
    # ex. /new_arrival
    path("new_arrival", views.new_arrival, name='new_arrival'),
]