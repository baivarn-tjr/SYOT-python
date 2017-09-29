from django.shortcuts import render
from django.http import HttpResponse

def product(request):
    context = locals()
    template = 'product.html'
    return render(request, template , context)

# def product(request):
#     return HttpResponse("<h1></>")
