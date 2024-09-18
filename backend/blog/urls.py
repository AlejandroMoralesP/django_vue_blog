from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('posts/', PostListView.as_view()),
    path('posts/<post_slug>/', PostDetailView.as_view()),
]