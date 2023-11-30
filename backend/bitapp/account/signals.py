from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models



@receiver(post_save, sender=models.User)
def create_user_profile(sender, instance, created, **kwargs):
    print(created)
    if created:
        models.UserProfile.objects.create(user=instance)
        print('user profile is created.')    
    else:
        try:
            profile = models.UserProfile.objects.get(user=instance)
            profile.save()
            print('user is updated')    
        except:
            # create user profile is it dosn't exist
            models.UserProfile.objects.create(user=instance)
            print('Profile did not exist, but i created one now.')