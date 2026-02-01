from django.urls import path
from . import views

app_name = 'chat' # Good practice for namespacing

urlpatterns = [
    # Main Chat Room
    path('<int:swap_id>/', views.chat_room, name='chat_room'),
    
    # API Endpoints for Notifications
    path('api/unread-total/', views.api_unread_count, name='api_unread_count'),
    path('api/unread-counts/', views.get_unread_counts, name='get_unread_counts'),
]