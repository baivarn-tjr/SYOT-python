from django import forms
from .models import Applicant
from django.core.validators import RegexValidator

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

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
