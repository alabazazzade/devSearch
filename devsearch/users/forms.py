from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import profile

class profileform(ModelForm):
    class Meta:
        model = profile
        fields =['name','email','bio','location',
        'profile_image','social_twitter',
        'social_github','social_youtube','short_intro']

    def __init__(self, *args, **kwargs):
      super(profileform, self).__init__(*args, **kwargs)
      self.fields['name'].widget.attrs.update({'class':'input'})  
      self.fields['email'].widget.attrs.update({'class':'input'})  
      self.fields['location'].widget.attrs.update({'class':'input'})  
      self.fields['short_intro'].widget.attrs.update({'class':'input'})  
      self.fields['bio'].widget.attrs.update({'class':'input'}) 
      self.fields['profile_image'].widget.attrs.update({'class':'input'}) 
      self.fields['social_twitter'].widget.attrs.update({'class':'input'}) 
      self.fields['social_github'].widget.attrs.update({'class':'input'}) 
      self.fields['social_youtube'].widget.attrs.update({'class':'input'}) 



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name',
        }

    def __init__(self, *args, **kwargs):
      super(CustomUserCreationForm, self).__init__(*args, **kwargs)
      self.fields['first_name'].widget.attrs.update({'class':'input'})  
      self.fields['email'].widget.attrs.update({'class':'input'})  
      self.fields['username'].widget.attrs.update({'class':'input'})  
      self.fields['password1'].widget.attrs.update({'class':'input'})  
      self.fields['password2'].widget.attrs.update({'class':'input'})  