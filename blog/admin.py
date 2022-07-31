from pydoc import classname
from django.contrib import admin
from .models import BlogModel, CardModel

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ("nom", "prenom", "email", "telephone")

admin.site.register(BlogModel, BlogAdmin)
admin.site.register(CardModel)