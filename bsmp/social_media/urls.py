from django.urls import path
from . import views

urlpatterns = [
    path('', views.social_media, name='social_media'),
    path('post/<int:id>/', views.single_post, name='single_post'),
    path('post/update/<int:id>/', views.update_post, name='update_post'),
    path('post/delete/<int:id>/', views.delete_post, name='delete_post'),
    path('post/<int:id>/comment/', views.create_comment, name='create_comment'),
    path('comment/delete/<int:id>/', views.delete_comment, name='delete_comment'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('category/<str:category_name>/', views.posts_by_category, name='posts_by_category'),
    path('create_post/', views.create_post, name='create_post'),
    path('post/<int:id>/like/', views.like_post, name='like_post'),
]