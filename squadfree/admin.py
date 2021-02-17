from django.contrib import admin
from .models import Item, Details

# class AuthorAdmin(admin.ModelAdmin):
   # pass

admin.site.register(Item)
admin.site.register(Details)

