from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aid/', include('aid.urls')),
    path('', lambda request: redirect('aid/')),
    path('api/', include('aid.api_urls')),
]
