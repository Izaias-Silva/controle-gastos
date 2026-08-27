from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Categoria, Gasto

admin.site.register(Categoria)
admin.site.register(Gasto)