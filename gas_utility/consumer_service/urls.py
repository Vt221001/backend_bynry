from django.urls import path
from .views.authentication import register, login
from .views.service_requests import create_service_request, list_service_requests, update_service_request_status
from .views.feedback import submit_feedback, list_feedback

urlpatterns = [
    # Authentication
    path('register/', register, name='register'),
    path('login/', login, name='login'),

    # Service Requests
    path('service-requests/', list_service_requests, name='list_service_requests'),
    path('service-requests/create/', create_service_request, name='create_service_request'),
    path('service-requests/update/<int:pk>/', update_service_request_status, name='update_service_request_status'),

    # Feedback
    path('feedback/', list_feedback, name='list_feedback'),
    path('feedback/submit/', submit_feedback, name='submit_feedback'),
]
