from django.urls import path
from mainpage import views
from mainpage.views import (
    FeedListView,
    FeedDetailView,
    FeedCreateView,
    FeedUpdateView,
    FeedDeleteView
)

urlpatterns = [
    path('', views.home, name='main-home'),
    path('post/<int:pk>/', FeedDetailView.as_view(), name='feed-detail'),
    path('post/new/', FeedCreateView.as_view(), name='feed-create'),
    path('post/<int:pk>/update/', FeedUpdateView.as_view(), name='feed-update'),
    path('post/<int:pk>/delete/', FeedDeleteView.as_view(), name='feed-delete'),
]