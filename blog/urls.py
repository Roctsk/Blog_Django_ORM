from django.urls import path
from blog.views import post_list
from . import views

urlpatterns = [
    path('',post_list, name = 'post_list' ),
    path("post/<int:pk>/", views.post_detail,name ="post_detail"),
    path("autohr/<int:author_id>/", views.post_by_author,name ="post_by_author"),
]