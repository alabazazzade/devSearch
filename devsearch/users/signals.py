from .models import profile
from projects.models import Project
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

@receiver(post_save, sender=User)
def createprofile(sender, instance, created, **kwargs):
    if created:
        print('created')
        user = instance
        Profile = profile.objects.create(
            user=user,
            email=user.email,  
        ) 


@receiver(post_delete, sender=profile)
def profileDeleted(sender, instance,**kwargs):
    user = instance.user
    user.delete()

# post_save.connect(profileUpdated, sender=profile)
# post_delete.connect(profileDeleted, sender=profile)