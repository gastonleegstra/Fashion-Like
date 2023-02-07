from django.contrib import admin
from .models import UserProfile #se coloca . para indicar que esta en el mismo directorio
# Register your models here.

admin.site.register(UserProfile)