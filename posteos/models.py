from django.utils import timezone
from django.db import models
from users.models import User
from django.conf import settings

# Create your models here.
def photo_up_path(instance,filename):
    return '{0}'.format(filename)

class Image(models.Model):
    image = models.ImageField(upload_to=photo_up_path, blank=True, null=True)


class Post(models.Model):
    title = models.TextField()
    description = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name='post_author')
    image = models.ManyToManyField(Image, blank=True)
    created = models.DateTimeField(default=timezone.now)
    dislikes = models.ManyToManyField(User, blank=True,related_name='dislikes')
    likes = models.ManyToManyField(User,blank=True,related_name='likes')

    class Meta:
        ordering = ['-created'] 

    def __str__(self):
        return self.author.username + ' : ' + self.title




