from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Applicant
from .forms import LoginForm , ForgotPasswordForm , ResetPasswordForm
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.contrib.auth.hashers import make_password

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
    success = False
    err = False
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Applicant.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token) and user.reset_password == 'RS':
        user.is_activated = 'WT'
        if request.method == 'POST':
            form = ResetPasswordForm(request.POST)
            if form.is_valid():
                new_password = request.POST['new_password']
                user.set_password(new_password)
                # user.password = make_password(new_password)
                user.is_activated = 'AC'
                user.reset_password = 'CL'
                user.save()
                success = 'Reset password is complete.'
        else:
            form = ResetPasswordForm()
            # context = {
            # }
            # return render(request, 'start.html' , context)
    else:
        form = ResetPasswordForm()
        err = 'Activation link is invalid!'

    return render(request, 'reset_password.html', {'form': form, 'uidb64': uidb64,
                                                   'token': token, 'err': err, 'success': success})





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
            user.reset_password = 'RS'
            user.save()
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
        return render(request, 'forgot-password.html' , context)
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
