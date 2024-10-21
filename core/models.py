from django.db import models

# Create your models here.
from django.db import models
from users.models import User


class DynamicModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # User owning the model
    model_name = models.CharField(max_length=100)  # Name of the model
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_name


class FieldSchema(models.Model):
    dynamic_model = models.ForeignKey(
        DynamicModel, related_name="fields", on_delete=models.CASCADE
    )
    field_name = models.CharField(max_length=100)
    field_type = models.CharField(
        max_length=50
    )  # Store types like "CharField", "IntegerField", etc.
    required = models.BooleanField(default=False)
    unique = models.BooleanField(default=False)
    default_value = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.field_name} ({self.field_type})"
