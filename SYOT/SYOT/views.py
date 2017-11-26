from django.shortcuts import render
from django.http import HttpResponse
from products.models import Product
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def index(request):
    products = Product.objects.all().order_by('?')[:4]
    count = 0
    context = {
        'product' : products,
        'count' : count,
    }
    return render(request, 'homepage.html' , context)

def about(request):
    succes = False
    try:
        data = request.POST
        name = data['name']
        email = data['email']
        sub = data['subject']
        comment = data['text']
        message = render_to_string('contact_email.html', {
            'name' : name,
            'comment' : comment,
            'email' : email
        })
        mail_subject = sub
        to_email = 'syotshopbkk@gmail.com'
        email = EmailMessage(mail_subject, message, to=[to_email])
        email.send()
        succes = "Thank you"
    except KeyError:
        pass

    context = {
        'suc' : succes
    }
    return render(request, 'about.html' , context)
