from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import geneare_code
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user=models.OneToOneField(User,related_name='profile_user',on_delete=models.CASCADE)
    image=models.ImageField(upload_to='photo_user')
    code=models.CharField(max_length=75,default=geneare_code)

    def __str__(self):
        return str(self.user)
    

# create new profile if create new user
@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )
    

