from django.urls import path

from . import views

urlpatterns = [
    path("pol", views.index, name="index"),
    path("january", views.january, name="january"),
    path("<month>", views.monthly_challenge, name="monthly_challenge"),

]
