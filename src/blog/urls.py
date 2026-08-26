from django.urls import path

from . import views

app_name = "blog"
urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("pol", views.pol, name="pol"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
    # path("<str:month>", views.monthly_challenge, name="month_str_path"),

]
