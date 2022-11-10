from .models import profile
from projects.models import Project
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from devsearch import settings

@receiver(post_save, sender=User)
def createprofile(sender, instance, created, **kwargs):
    if created:
        print('created')
        user = instance
        Profile = profile.objects.create(
            user=user,
            email=user.email,  
        ) 

        subject = 'Welcome to devsearch'
        body = f'Thank you for creating an account in our website!' + '\n' + 'devSearch team'
        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,
            [Profile.email],
            fail_silently=False,
        )

@receiver(post_save, sender=profile)
def updateuser(sender, instance,created, **kwargs):
    profile = instance 
    user = profile.user
    
    if created == False:
        user.first_name = profile.name
        # user.username = profile.username
        user.email = profile.email
        user.save()


@receiver(post_delete, sender=profile)
def profileDeleted(sender, instance,**kwargs):
    user = instance.user
    user.delete()

# post_save.connect(profileUpdated, sender=profile)
# post_delete.connect(profileDeleted, sender=profile)