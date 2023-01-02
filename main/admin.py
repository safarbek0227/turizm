from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(MainPage)

admin.site.register(TravelTicket)

admin.site.register(Picture)

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ["title"]
    prepopulated_fields = {"slug":("title",)}