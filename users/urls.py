from django.urls import path
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from . import views

urlpatterns = [
    # 1. Jab koi sirf 'users/' likhe, use login par bhej do (404 fix)
    path('', lambda request: redirect('login'), name='users_root'),

    # 2. Authentication & Profile
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    
    # 3. Password Reset Flow
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'), 
         name='password_reset'),
         
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), 
         name='password_reset_done'),
         
    path('password-reset/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'), 
         name='password_reset_confirm'),
         
    path('password-reset/complete/', 
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), 
         name='password_reset_complete'),
]