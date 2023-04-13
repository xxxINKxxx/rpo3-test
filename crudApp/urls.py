from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('post/view/<int:pk>/', views.postDetail, name='postDetail'),
    path('about/', views.aboutpage, name='aboutpage'),
 ]