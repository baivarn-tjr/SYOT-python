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
    user = Applicant.objects.get(username=username)


    if not applicant :
        context = {
            'errorMess' : 'wrong user',
        }
        return render(request, 'login.html' , context)

    elif applicant.check_password(password) :
        context = {
            # 'loginConfirm' : 'yes',
            'appli' : applicant.username,
            }
        request.session['user_id'] = user.id
        return render(request, 'index.html' , context)
    else :
        context = {
            'errorMess' : 'wrong pass',
        }
        return render(request, 'login.html' , context)
