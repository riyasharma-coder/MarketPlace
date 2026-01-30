from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect # Already imported

urlpatterns = [
    # Root URL: Jab koi 127.0.0.1:8000 kholay, use exchange par bhej do.
    # Hum 'item_list' (jo exchange/urls.py mein hai) ka use karenge.
    path('', lambda request: redirect('item_list'), name='home'),
    
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('exchange/', include('exchange.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('centers/', include('centers.urls')),
    path('community/', include('community.urls')),
]

# Static aur Media files serving
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)