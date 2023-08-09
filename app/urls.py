from django.urls import path
from . import views
urlpatterns = [
    path("",views.index),
    path('home/', views.home, name='home'),
    path('transform/<str:transformation>/', views.transform_text, name='transform_text'),]

