from django.urls import path

from . import views

app_name = "profiles"
urlpatterns = [
    path("create", views.CreateProfileView.as_view(), name="create"),
    path("list", views.ListProfileView.as_view(), name="list")
]
