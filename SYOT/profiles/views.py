from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader


from .models import Profile, Shipping

def loot(request):
    profile_list = Profile.objects.all()
    context = {
        'profile_list': profile_list,
    }
    return render(request, 'main.html', context)

def detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'profile.html', {'profile': profile})
