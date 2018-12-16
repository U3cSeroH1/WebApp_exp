from django.urls import path

from . import views

app_name = 'comment'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('detail/<int:pk>/',
        views.PostDetailView.as_view(), name='post_detail'),
    path('comment/<int:pk>/',
        views.CommentView.as_view(), name='comment'),
    path('reply/<int:pk>/',
        views.ReplyView.as_view(), name='reply'),
]