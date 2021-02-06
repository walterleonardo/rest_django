from django.contrib import admin
from .models import Product
# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","title", "description", "image", "updated")
    list_filter = ("title", )
    search_fields = ("title__startswith", )
    fields = ("title", "description", "image")
    class Meta:
        ordering = ("updated")