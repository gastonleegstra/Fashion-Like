from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


#genero ruta para guardar avatar
def photo_up_path(instance,filename):
    return '{0}/{1}'.format(instance.user.username,filename)

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.TextField(null=True,blank=True)
    profile_pic = models.ImageField(upload_to=photo_up_path, default='/default/default_avatar.jpg' )

    def __str__(self):
        return self.user.username

#Crea el Profile del usuario
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = UserProfile(user=instance)
        user_profile.save()

#Me suscribo a la señal post_save para lanzar el metodo de creado de profile
post_save.connect(create_profile,sender=User)
