from django import forms
from .models import Applicant
from django.core.validators import RegexValidator


class SignupForm(forms.Form):
    username = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'placeholder': 'username'}))
    email = forms.EmailField(required=True, max_length=128,widget=forms.TextInput(attrs={'placeholder': 'example@gmail.com'}))
    firstname = forms.CharField(required=True, max_length=128)
    lastname = forms.CharField(required=True, max_length=128)
    password = forms.CharField(
        required=True,
        min_length=8,
        max_length=128,
        widget=forms.PasswordInput,
        validators=[RegexValidator(
            regex='^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$',
            message='Password must contain at least one alphabet and one digit'
        )]
    )
    confirm_password = forms.CharField(
        required=True,
        widget=forms.PasswordInput
    )
    mobile = forms.CharField(
        required=True,
        max_length=10,
        min_length=10,
        validators=[RegexValidator(
            regex='^[0][0-9]*$',
            message='Phone number must be numeric 0-9 and Please lengthen phone number to 10.'
        ), ]
    )
    address = forms.CharField(
        required=True, max_length=128, widget=forms.Textarea())
    city = forms.CharField(required=True, max_length=128)
    state = forms.CharField(required=True, max_length=128)
    zipcode = forms.CharField(
        required=True,
        max_length=5,
        min_length=5,
        validators=[RegexValidator(
            regex='^[0-9]*$',
            message='Zip code must be numeric 0-9 and Please lengthen phone number to 5.'
        ), ]
    )

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 and password1 != password2:
            raise forms.ValidationError("Passwords don't match.")

        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Applicant.objects.filter(email=email):
            raise forms.ValidationError("Email is already taken.")
        return self.cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField( label = 'username',
                                max_length = 100)
    password = forms.CharField(
        label = 'password',
        max_length = 100,
        widget = forms.PasswordInput,
        # validators=[RegexValidator(
        #     regex='^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$',
        #     message='Password must contain at least one alphabet and one digit'
        #     )]
    )

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
        validators=[RegexValidator(
            regex='^(?=.*[0-9])(?=.*[a-zA-Z])([a-zA-Z0-9]+)$',
            message='Password must contain at least one alphabet and one digit'
        )]

    )
    confirm_password = forms.CharField(
        required=True, widget=forms.PasswordInput)

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('new_password')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 and password1 != password2:
            raise forms.ValidationError("Password don't match.")

        return self.cleaned_data
