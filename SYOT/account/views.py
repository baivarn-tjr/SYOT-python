from django.shortcuts import render
from django.http import HttpResponse
from .models import Applicant

def login(request):
    context = {
    }
    return render(request, 'login.html' , context)

def signup(request):
    context = {
    }
    return render(request, 'signup.html' , context)

def create_applicant(form):
    applicant = Applicant(
                            username = form['user'],
                            tel = form['tel'],
                            email = form['email'])
    applicant.set_password(form['pass'])
    applicant.save()

def signupCheck(request):
    context = {
    }
    form = request.POST
    create_applicant(form)
    return render(request, 'index.html' , context)

def loginCheck(request):
    form = request.POST
    username = form['user']
    password = form['pass']
    applicant = Applicant.find_by_username(username)

    if not applicant:
        context = {
            'errorMess' : 'worng',
        }
        return render(request, 'login.html' , context)
    else :
        context = {
            'loginConfirm' : 'yes',
        }
        return render(request, 'index.html' , context)
