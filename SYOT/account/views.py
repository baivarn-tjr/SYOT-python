from django.shortcuts import render
from django.http import HttpResponse
from .models import Applicant

def login(request):
    # print("in")
    context = {
    }
    return render(request, 'login.html' , context)

def test(request):
    # print("in")
    context = {
    }
    return render(request, 'start.html' , context)

def loginCheck(request):
    # print("in")
    context = {
    }
    form = request.POST
    username = form['user']
    password = form['pass']
    applicant = Applicant.find_by_username(username)
    if not applicant:
        return HttpResponse("Not have username")
    else :
        return HttpResponse("Hello, world. You're at the polls index.")
