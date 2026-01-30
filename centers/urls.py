from django.urls import path
from . import views

urlpatterns = [
    path('map/', views.center_map_view, name='map_view'),
]