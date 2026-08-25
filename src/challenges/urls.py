from django.urls import path

from . import views

# name attribute used fpr reverse URL -> with redirect(name,string)
app_name = "challenges" # set to solve path name comflicts with % url 'challenges:index' tag
urlpatterns = [
    path("", views.index, name="index"),
    path("pol", views.pol, name="pol"),
    path("<int:month>", views.monthly_challenge_by_number, name="monthly_challenge_number"),
    path("<str:month>", views.monthly_challenge, name="month_str_path"),

]
