from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Custom User Model
class User(AbstractUser):
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()

    # Fixing group and permission conflicts
    groups = models.ManyToManyField(Group, related_name="custom_user_set", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions_set", blank=True)

    def __str__(self):
        return self.username  # Display username instead of object ID

# Service Request Model
class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="service_requests")
    request_type = models.CharField(max_length=100, default="General Inquiry")
    details = models.TextField()
    attachment = models.FileField(upload_to='attachments/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    submitted_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Service Requests"  # Admin panel name fix

    def __str__(self):
        return f"{self.request_type} - {self.status}"

# Feedback Model
class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="feedbacks")
    service_request = models.ForeignKey(ServiceRequest, on_delete=models.CASCADE, related_name="feedbacks")
    rating = models.IntegerField()  # Keeping it simple (should be 1-5)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback by {self.user.username} - {self.rating} Stars"
