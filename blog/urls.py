from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('<int:pk>/', views.full_post, name="full_post"),
    path('Category/<category>/', views.category, name="category"),
    path('Search/', views.Search, name="Search"),
    path('Reply/<int:pk>/', views.Replies, name="Reply")
]