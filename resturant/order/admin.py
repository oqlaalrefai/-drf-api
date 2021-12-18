from django.contrib import admin
from .models import order


@admin.register(order)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['foodName', 'content', 'times']
