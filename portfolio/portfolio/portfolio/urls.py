from django.contrib import admin
from django.urls import path, include  # Import 'include'

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('', include('Base.urls')),  # Include Base app's URL patterns
]
