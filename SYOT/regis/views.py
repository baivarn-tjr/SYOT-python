from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ValidationError
from django import forms
from django.conf import settings
from .models import Applicant
from django.http import HttpResponseForbidden
from django.urls import reverse

class LoginForm(forms.Form):
    username = forms.CharField( label = 'username',
                                max_length = 100)
    password = forms.CharField( label = 'password',
                                max_length = 100,
                                widget = forms.PasswordInput)

class RegistrationForm(forms.Form):

    prefix = forms.ChoiceField(label = 'gender',
                                choices=[
                                    ('male', 'male'),
                                    ('female', 'female'),
                                ])

    username = forms.CharField(   label = 'username',
                                    max_length = 100)
    tel = forms.CharField(   label = 'tel',
                                    max_length = 100)

    email = forms.EmailField(label = 'email')
    password = forms.CharField(     label = 'password',
                                    max_length=100,
                                    widget=forms.PasswordInput)

    password_confirm = forms.CharField(     label = 'password(again)',
                                            max_length=100,
                                            widget=forms.PasswordInput)

    @staticmethod
    def is_valid_tel(tel):
        a = tel
        if(a[0] != '0'):
            return False
        for c in tel:
            if c > '9' or c < '0':
                return False

        if (len(tel) != 9) and (len(tel) != 10):
            return False

        return True

    def clean_tel(self):
        
        if not RegistrationForm.is_valid_tel(self.cleaned_data['tel']):
            del self.cleaned_data['tel']
            raise ValidationError('not in forms', code='invalid')
        return self.cleaned_data['tel']

    def clean_password_confirm(self):
        if self.cleaned_data['password_confirm'] != self.cleaned_data['password']:
            del self.cleaned_data['password_confirm']
            raise ValidationError('password dose not match', code='invalid')

def create_applicant(form):
    applicant = Applicant(  prefix = form.cleaned_data['prefix'],
                            username = form.cleaned_data['username'],
                            tel = form.cleaned_data['tel'],
                            email = form.cleaned_data['email'])
    applicant.set_password(form.cleaned_data['password'])
    try:
        applicant.save()
        return True
    except:
        return False

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            if create_applicant(form):
                return redirect(reverse('main-index'))
            else:
                return render(request, 'regis/registration_error.html',
                                {   'username' : form.cleaned_data['username'],
                                    'email': form.cleaned_data['email']})
    else:
        form = RegistrationForm()
    return render(  request,
                    'regis/register.html',
                    { 'form':form })

def login_applicant(request, applicant):
    request.session['applicant_id'] = applicant.id

def login(request):
    if request.method != 'POST':
        return HttpResponseForbidden()

    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        applicant = Applicant.find_by_username(username)
        if not applicant:
            return redirect(reverse('main-index') + '?error=wrong-password')

        if applicant.check_password(password):
            login_applicant(request, applicant)
            return redirect(reverse('regis:apptemp'))
        else:
            return redirect(reverse('main-index') + '?error=wrong-password')
    else:
        return redirect(reverse('main-index') + '?error=invalid')

def logout(request):
    if 'applicant_id' in request.session:
        del request.session['applicant_id']
    return redirect(reverse('main-index'))

def apptemp(request):
    if 'applicant_id' not in request.session:
        return redirect(reverse('main-index') + '?error=no-login')

    applicant_id = request.session['applicant_id']
    applicant = get_object_or_404(Applicant, pk=applicant_id)
    return render(request,
                    'regis/apptemp.html',
                    {'applicant' : applicant})
