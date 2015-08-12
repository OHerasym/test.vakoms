from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from app1.models import UserProfile

class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = UserProfile
        fields = ('email', 'mobile', 'first_name', 'last_name','password1', 'password2')
        
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        
        if commit:
            user.is_active = False
            user.save()
            
        return user