from django.shortcuts import render
from django.http import HttpResponse

def favorite(request):
    context = locals()
    template = 'favorite/favorite.html'
    return render(request, template , context)
