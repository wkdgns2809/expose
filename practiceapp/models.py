from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class SJH(models.Model) :
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length = 200)
    Textarea = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)
    category = models.CharField(max_length = 50, blank=True)
    pic = models.ImageField(upload_to="images/",null=True)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50,blank=True)
    region = models.CharField(max_length=50,blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()