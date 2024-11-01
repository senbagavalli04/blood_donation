# django_blood_app/urls.py
from django.contrib import admin
from django.urls import path, include  # include is necessary to include app URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('prediction.urls')),  # Include the prediction app's URLs
    path('', include('prediction.urls')),  # Add this line to include the prediction page
]
