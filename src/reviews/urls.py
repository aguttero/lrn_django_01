from django.urls import path

from . import views

app_name = "reviews"
urlpatterns = [
     # path("", views.review, name="review"), #V01 y V02
     path("", views.ReviewView.as_view(), name="review"), #V03 View Class
     # path("thankyou", views.thank_you, name="thank_you")
     path("thankyou", views.ThankYouView.as_view(), name="thank_you"),
     path("reviewlist", views.ReviewsListView.as_view(), name="review_list"),
     path("item/<int:pk>", views.ReviewItemView.as_view(), name="review_detail")
]
