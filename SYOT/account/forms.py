from django import forms
from .models import Applicant
from django.core.validators import RegexValidator


class LoginForm(forms.Form):
    username = forms.CharField( label = 'username',
                                max_length = 100)
    password = forms.CharField( label = 'password',
                                max_length = 100,
                                widget = forms.PasswordInput)

class ForgotPasswordForm(forms.Form):
    email = forms.EmailField( label = 'email', required=True, max_length=128)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not Applicant.objects.filter(email=email):
            raise forms.ValidationError("Email does not exist.")
        return self.cleaned_data

class ResetPasswordForm(forms.Form):
    new_password = forms.CharField(
        required=True,
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput,

    )
    confirm_password = forms.CharField(
        required=True, widget=forms.PasswordInput)

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('new_password')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 and password1 != password2:
            raise forms.ValidationError("Password don't match.")

        return self.cleaned_data
