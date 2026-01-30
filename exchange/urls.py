from django.urls import path
from . import views

urlpatterns = [
    # Home & Listing views
    path('', views.item_list_view, name='item_list'), 
    path('home/', views.home_view, name='home'),
    
    # Item Management
    path('add/', views.add_item_view, name='add_item'),
    path('item/<int:pk>/', views.item_detail_view, name='item_detail'),
    path('my-listings/', views.my_listings_view, name='my_listings'),
    path('item/delete/<int:pk>/', views.delete_item_view, name='delete_item'),
    
    # Swap Interaction (The Fix)
    # Changed name from 'send_request' to 'send_swap_request' to match your template
    path('item/<int:item_id>/request/', views.send_swap_request, name='send_swap_request'),
    
    # Dashboard & Status Updates
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Updated to match 'update_request_status' logic in your views
    path('request/<int:req_id>/<str:new_status>/', views.update_request_status, name='update_status'),
]