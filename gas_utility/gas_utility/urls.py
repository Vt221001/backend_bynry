from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

# Define a simple home view
def home_view(request):
    return HttpResponse("<h1>Welcome to Gas Utility Service API</h1>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('consumer_service.urls')),  # Include your app URLs
    path('', include('consumer_service.urls')),
]
