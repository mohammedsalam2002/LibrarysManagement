from django.contrib import admin

# Register your models here.
from . models import Books
admin.site.register(Books)
from . models import Category
admin.site.register(Category)