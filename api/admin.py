from django.contrib import admin
from .models import Contacts 

@admin.register(Contacts)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']
    list_filter = ['name', 'email', 'phone']
    list_fields = ['name', 'email', 'phone']