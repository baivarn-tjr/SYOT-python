from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Applicant
from .forms import NameForm

def get_name(request):
    context = {
    }
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'forgot-password.html' , context)

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

def forgot(request):
    context = {
    }
    return render(request, 'forgot-password.html' , context)


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
        request.session.set_expiry(1800)
        return render(request, 'homepage.html' , context)
    else :
        context = {
            'errorMess' : 'wrong pass',
        }
        return render(request, 'login.html' , context)
