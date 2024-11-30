from django.shortcuts import render
from .models import Profile

def about_me(request):
    profile = Profile.objects.first()  # Fetch the first profile
    return render(request, 'aboutme/about_me.html', {'profile': profile})
