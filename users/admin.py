from django.contrib import admin
#se coloca . para indicar que esta en el mismo directorio
from .models import UserProfile, User 

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)