from django.urls import path

from . import views

# name attribute used fpr reverse URL -> with redirect(name,string)
urlpatterns = [
    path("", views.index_old, name="index"),
    path("pol", views.pol, name="pol"),
    path("healthy", views.healthy, name="healthy"),
    path("<int:month>", views.monthly_challenge_by_number, name="monthly_challenge_number"),
    path("<str:month>", views.monthly_challenge, name="month_str_path"),

]
