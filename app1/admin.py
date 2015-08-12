from django.contrib import admin
from django.contrib.auth.models import Group
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from app1.models import UserProfile

import re

class UserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label = 'Type Password', widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)

	class Meta:
		model = UserProfile
		fields = ['email', 'mobile', 'first_name', 'last_name', 'is_active']

		def clean_password2(self):
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']

			if password1 and password2 and password1 != password2:
				raise forms.ValidationError('Passwords does not match!')
			return password2

		def save(self, commit=True):
			user = super(UserCreationForm, self).save(commit = False)
			user.set_password(self.cleaned_data['password1'])
			user.save()
			return user


class UserChangeForm(forms.ModelForm):
	password = ReadOnlyPasswordHashField()

	class Meta:
		model = UserProfile
		fields = ['email', 'mobile', 'first_name', 'last_name', 'is_active']

	def clean_password(self):
		return self.initial['password']



class UserProfileAdmin(UserAdmin):
	form = UserChangeForm
	add_form = UserCreationForm

	list_display = ['email', 'mobile', 'first_name', 'last_name', 'is_active']
	list_filter = ['email',]
	ordering = ['email', ]

	fieldsets = (
					(None, {'fields':('email', 'first_name','last_name','password',)}),
		)

	add_fieldsets = (
						(None, {'fields': ('email', 'mobile', 'first_name','password1', 'password2')})
		)

	filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(UserProfile, UserProfileAdmin)