from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Applicant, Shipping
from .forms import LoginForm , ForgotPasswordForm , ResetPasswordForm , SignupForm
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


def profile(request):
    try:
        uid = request.session['user_id']
    except KeyError:
        pass
    user = Applicant.objects.get(id=uid)
    product_list = user.myShipping.all()
    shipping_list = Shipping.objects.all()
    context = {
        'user' : user,
        'product_list' : product_list,
        'shipping_list' : shipping_list,
        'firstN' : user.firstname,
        'lastN' :  user.lastname,
        'username' : user.username,
        'email' : user.email,
        'mobile' : user.mobile,
        'address' : user.address,
        'city' : user.city,
        'state' : user.state,
        'zip' : user.zipcode,
    }
    return render(request,'profile.html',context)

def signup(request):
    form = False
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            applicant = Applicant(
                                    username = request.POST['username'],
                                    email = request.POST['email'],
                                    firstname = request.POST['firstname'],
                                    lastname = request.POST['lastname'],
                                    mobile = request.POST['mobile'],
                                    address = request.POST['address'],
                                    city = request.POST['city'],
                                    state = request.POST['state'],
                                    zipcode = request.POST['zipcode'])
            applicant.set_password(request.POST['password'])
            applicant.save()
            success = 'Please confirm your email address to complete the registration.'
            user = Applicant.objects.get(email=request.POST['email'])
            token = account_activation_token.make_token(user)
            user.token = token
            user.save()
            domain = 'http://localhost:8000'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            message = render_to_string('activated_account_email.html', {
                'user': user,
                'domain': domain,
                'uid': uid,
                'token': token,
            })
            mail_subject = 'Activated your account'
            to_email = request.POST['email']
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            # success = 'Please check your email.'
            form = ForgotPasswordForm()
            return render(request,'signup.html', {'success': success})

    else:
        form = SignupForm()

    context = {
        'form' : form
    }
    return render(request, 'signup.html' , context)

def activated_acc(request,uidb64,token):
    success = False
    err = False
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Applicant.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_activated = 'AC'
        user.save()
        success = 'Activated is complete !\nWelcome to SYOT.'

    else:
        err = 'Activation link is invalid!'

    return render(request, 'activated_account.html', {'uidb64': uidb64,
                                                   'token': token, 'err': err, 'success': success})

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

        if applicant.check_password(password) and user.is_activated == 'AC':
            context = {
                }
            request.session['user_id'] = user.id
            request.session['user_name'] = user.username
            request.session.set_expiry(1800)
            return render(request, 'homepage.html' , context)

        elif applicant.check_password(password) and user.is_activated != 'AC':
            login_form = LoginForm()
            context = {
                'error_message' : 'Please activated account',
                'login_form' : login_form
            }
            return render(request, 'login.html' , context)
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
