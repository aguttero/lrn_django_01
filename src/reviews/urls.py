from django.urls import path

from . import views

app_name = "reviews"
urlpatterns = [
     # path("", views.review, name="review"), #V01 y V02
     path("", views.ReviewView.as_view(), name="review"), #V03 View Class
     path("thankyou", views.thank_you, name="thank-you")
]
