from django.shortcuts import render
from django.http import HttpResponse
from .models import Applicant

def login(request):
    context = {
    }
    return render(request, 'login.html' , context)

def logout(request):
    context = {
    }
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return render(request, 'homepage.html' , context)


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
    return render(request, 'homepage.html' , context)

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
        request.session['user_name'] = user.username
        return render(request, 'homepage.html' , context)
    else :
        context = {
            'errorMess' : 'wrong pass',
        }
        return render(request, 'login.html' , context)
