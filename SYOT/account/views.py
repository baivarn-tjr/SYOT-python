from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Applicant
from .forms import LoginForm , ForgotPasswordForm
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password

# def get_name(request):
#     context = {
#     }
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'forgot-password.html' , context)

def login(request):
    login_form = LoginForm()
    context = {
        'login_form' : login_form ,
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

def reset_password(request,uidb64,token):
    return render(request,'reset_password.html',{})


def forgot(request):
    form = ForgotPasswordForm()
    context = {
        'form' : form ,
    }
    return render(request, 'forgot-password.html' , context)

def forgotCheck(request):
    err = False
    success = False
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            # user = request.POST['email']
            user = Applicant.objects.get(email=request.POST['email'])
            token = account_activation_token.make_token(user)
            user.token = token
            domain = 'http://localhost:8000'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            message = render_to_string('reset_password_email.html', {
                'user': user,
                'domain': domain,
                'uid': uid,
                'token': token,
            })
            mail_subject = 'Reset your password'
            to_email = request.POST['email']
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            success = 'Please check your email.'
            form = ForgotPasswordForm()

    else:
        err = 'Please enter your email address to retrieve your password.'
        form = ForgotPasswordForm()
        context = {
            'form' : form,
            'err' : err,
        }
    context = {
        'form' : form,
        'err' : err,
        'success' : success,
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
    if request.method != 'POST':
        return HttpResponseForbidden()

    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        applicant = Applicant.find_by_username(username)
        if applicant:
            user = Applicant.objects.get(username=username)

        if not applicant :
            login_form = LoginForm()
            context = {
                'error_message' : 'wrong-password',
                'login_form' : login_form
            }
            return render(request, 'login.html' , context)

        if applicant.check_password(password) :
            context = {
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
            return render(request , 'login.html' , context)

    else:
        context = {
            'error_message' : 'invalid',
        }
        return render(request, 'login.html' , context)

# def loginCheck(request):
#     form = request.POST
#     username = form['user']
#     password = form['pass']
#     applicant = Applicant.find_by_username(username)
#
#     user = Applicant.objects.get(username=username)
#
#
#     if not applicant :
#         context = {
#             'errorMess' : 'wrong user',
#         }
#         return render(request, 'login.html' , context)
#
#     elif applicant.check_password(password) :
#         context = {
#             # 'loginConfirm' : 'yes',
#             'appli' : applicant.username,
#             }
#         request.session['user_id'] = user.id
#         request.session['user_name'] = user.username
#         request.session.set_expiry(1800)
#         return render(request, 'homepage.html' , context)
#     else :
#         context = {
#             'errorMess' : 'wrong pass',
#         }
#         return render(request, 'login.html' , context)
