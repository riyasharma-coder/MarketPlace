from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect 
from exchange import views as exchange_views # Home page view ke liye

urlpatterns = [
    # 1. Main Home Page (Landing Page)
    path('', exchange_views.home_view, name='home'),
    
    # 2. Admin Panel
    path('admin/', admin.site.urls),
    
    # 3. Application Modules
    path('users/', include('users.urls')),
    path('exchange/', include('exchange.urls')),
    path('centers/', include('centers.urls')),
    path('community/', include('community.urls')),
    
    # 4. Authentication (Logout)
    # Note: next_page='home' par bhej rahe hain logout ke baad
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]

# 5. Media & Static Files (Development Mode)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)