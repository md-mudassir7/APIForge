from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import DynamicModel, FieldSchema


class FieldSchemaInline(admin.TabularInline):
    model = FieldSchema


class DynamicModelAdmin(admin.ModelAdmin):
    inlines = [FieldSchemaInline]


admin.site.register(DynamicModel, DynamicModelAdmin)
