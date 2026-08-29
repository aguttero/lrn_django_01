from django.urls import path

from . import views

app_name = "reviews"
urlpatterns = [
     path("", views.review, name="review"),
     path("thankyou", views.thank_you, name="thank-you")
]
