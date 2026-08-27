from django.urls import path

from . import views

app_name = "book_outlet"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.book_detail, name="book-detail"),
    path("pol", views.pol, name="pol")

]
