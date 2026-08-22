from django.urls import path

from . import views

urlpatterns = [
    path("pol", views.index, name="index"),
    path("healthy", views.healthy, name="healthy"),
    path("<int:month>", views.monthly_challenge_by_number, name="monthly_challenge_number"),
    path("<str:month>", views.monthly_challenge, name="monthly_challenge"),

]
