from django.urls import path
from . import views

app_name = 'anime'

urlpatterns = [
    path('', views.anime_list, name='anime_list'),
    path('<int:anime_id>/', views.anime_detail, name='anime_detail'),
]
