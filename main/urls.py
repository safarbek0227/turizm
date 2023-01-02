from django.urls import path
from .import views

app_name = "main"
urlpatterns = [
    path('', views.homeView, name="index"),
    path('detail/<pk>/', views.detail.as_view(), name="detail"),
]