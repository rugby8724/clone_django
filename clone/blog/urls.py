from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/', views.PostListView.as_view(), name='post_list'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('post/<int:pk/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/update/<int:pk>', views.UpdatePost.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='post_remove')


]
