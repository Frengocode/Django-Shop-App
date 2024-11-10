from django.forms import ModelForm, TextInput, PasswordInput, EmailInput
from .models import CustomUser
from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={"placeholder": "Username"}))
    email = forms.CharField(widget=EmailInput(attrs={"placeholder": "Email"}))
    password1 = forms.CharField(widget=PasswordInput(attrs={"placeholder": "Password"}))
    password2 = forms.CharField(
        widget=PasswordInput(attrs={"placeholder": "Confirm Password"})
    )
    phone_number = forms.IntegerField(
        label="Phone Number"
    )  

    class Meta:
        model = CustomUser
        fields = ["username", "password1", "password2", "email", "phone_number"]


class UploadProfilePictureForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ["profile_picture"]
