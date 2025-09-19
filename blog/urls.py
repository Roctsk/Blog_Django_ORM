from django.urls import path
from blog.views import post_list
from . import views

urlpatterns = [
    path('', post_list, name='post_list'), 
    path("post/<int:pk>/", views.post_detail, name="post_detail"),
    path("author/<int:author_id>/", views.posts_by_author, name="posts_by_author")
]