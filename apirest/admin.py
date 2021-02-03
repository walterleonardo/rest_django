from django.contrib import admin
from .models import Csv
# Register your models here.

@admin.register(Csv)
class CsvAdmin(admin.ModelAdmin):
    # list_display = ('file_name','uploaded','activated')
    # list_filter = ("file_name", )
    # search_fields = ("file_name__startswith", )
    # fields = ("file_name", "activated")
    class Meta:
        ordering = ("uploaded")