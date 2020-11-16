from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('music/', views.music, name='music'),
    path('portfolio/', views.portfolio, name='portfolio'),
]
