from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets
from django.utils.translation import ugettext as _
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from django.db import transaction
from django.contrib.auth.forms import AuthenticationForm, UsernameField

from AuthPanel.models import PassitUser, WebsiteOwner, User

class CreateUserForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Set PIN', max_length=6, widget=forms.PasswordInput(attrs={'placeholder' : 'Enter your PIN'}))
    password2 = forms.CharField(label='Confirm PIN', max_length=6, widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm PIN'}))
    phone_number = forms.CharField(max_length=10, validators=[
                                    RegexValidator(r'^\d{1,10}$')], required=True, widget= forms.TextInput(attrs={'placeholder' : 'Enter your phone number'}))
    first_name = forms.CharField(max_length=64, required=True, widget= forms.TextInput(attrs={'placeholder' : 'First Name'}))
    last_name = forms.CharField(max_length=64, required=True, widget= forms.TextInput(attrs={'placeholder' : 'Last Name'}))

    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email' : forms.EmailInput(attrs={'placeholder' : 'Enter your Email'})
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        try:
            validate_password(password1, self.instance)
        except forms.ValidationError as error:

            # Method inherited from BaseForm
            self.add_error('password1', error)

        return password2

    @transaction.atomic
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.is_passituser = True
        user.set_password(self.cleaned_data["password1"])
        user.save()
        passituser = PassitUser.objects.create(user=user)
        passituser.phone_number = self.cleaned_data['phone_number']
        passituser.name = self.cleaned_data['first_name'] + " " + self.cleaned_data['last_name'] 
        passituser.save()
        return user

class WebsiteRegForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Set PIN', max_length=6, widget=forms.PasswordInput(attrs={'placeholder' : 'Enter your PIN'}))
    password2 = forms.CharField(label='Confirm PIN', max_length=6, widget=forms.PasswordInput(attrs={'placeholder' : 'Confirm PIN'}))
    phone_number = forms.CharField(max_length=10, validators=[
                                    RegexValidator(r'^\d{1,10}$')], required=True, widget= forms.TextInput(attrs={'placeholder' : 'Enter Contact Info'}))
    first_name = forms.CharField(max_length=64, required=True, widget= forms.TextInput(attrs={'placeholder' : 'First Name'}))
    last_name = forms.CharField(max_length=64, required=True, widget= forms.TextInput(attrs={'placeholder' : 'Last Name'}))
    domain = forms.URLField(max_length=64, required=True, widget= forms.TextInput(attrs={'placeholder' : 'Enter your Website Domain'}))

    class Meta:
        model = User
        fields = ['email']
        widgets = {
            'email' : forms.EmailInput(attrs={'placeholder' : 'Enter your Email'})
        }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")

        try:
            validate_password(password1, self.instance)
        except forms.ValidationError as error:

            # Method inherited from BaseForm
            self.add_error('password1', error)

        return password2

    @transaction.atomic
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.is_websiteowner = True
        user.set_password(self.cleaned_data["password1"])
        user.save()
        website = WebsiteOwner.objects.create(user=user)
        website.phone_number = self.cleaned_data['phone_number']
        website.owner_name = self.cleaned_data['first_name'] + " " + self.cleaned_data['last_name'] 
        website.domain = self.cleaned_data['domain']   
        website.save()
        return user

class AuthenticationForm(AuthenticationForm):
    username = UsernameField(
        label='Email',
        widget=forms.TextInput(attrs={'placeholder' : 'Enter your Email'})
    )
    password = forms.CharField(label='Enter PIN', max_length=6, widget=forms.PasswordInput(attrs={'placeholder' : 'Enter PIN'}))
    remember_me = forms.BooleanField(required=False, initial=False, widget=forms.CheckboxInput())