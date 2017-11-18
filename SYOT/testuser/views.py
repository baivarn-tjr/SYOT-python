from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ValidationError
from django import forms
from django.conf import settings
from account.models import Applicant
from django.http import HttpResponseForbidden
from django.urls import reverse

class LoginForm(forms.Form):
    username = forms.CharField( label = 'username',
                                max_length = 100)
    password = forms.CharField( label = 'password',
                                max_length = 100,
                                widget = forms.PasswordInput)

def loginIndex(request):
    # return render(request,'loginTest.html',{ })
    login_form = LoginForm()

    # if 'error' in request.GET:
    #     error_message = request.GET['error']
    # else:
    #     error_message = None

    return render(  request,
                    'loginTest.html',
                    {   'login_form' : login_form ,
                        })

def login(request):

    if request.method != 'POST':
        # return HttpResponseForbidden()
        context = {
            'error_message' : 'wrong-password',
        }
        return render(request, 'index.html' , context)

    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        # username = form['user']
        # password = form['pass']
        applicant = Applicant.find_by_username(username)
        if applicant:
            user = Applicant.objects.get(username=username)

        # applicant = Applicant.find_by_username(username)
        if not applicant :
            login_form = LoginForm()
            context = {
                'error_message' : 'wrong-password',
                'login_form' : login_form
            }
            return render(request, 'loginTest.html' , context)

        if applicant.check_password(password) :
            context = {
                # 'loginConfirm' : 'yes',
                # 'appli' : applicant.username,
                }
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            request.session.set_expiry(1800)
            return render(request, 'homepage.html' , context)
        else :
            login_form = LoginForm()
            context = {
                'error_message' : 'wrong-password',
                'login_form' : login_form
            }
            return render(request , 'loginTest.html' , context)

    else:
        context = {
            'error_message' : 'invalid',
        }
        return render(request, 'loginTest.html' , context)
