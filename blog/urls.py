from django.urls import path
from . import views
from django.views.generic import TemplateView
from blog.views import Emprestimo

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('emprestimo/', Emprestimo.as_view(), name='emprestimo'),
]