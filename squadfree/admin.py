from django.contrib import admin
from .models import Item

class AuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Item)