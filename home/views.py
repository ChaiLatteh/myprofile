from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Story

# Create your views here.
def home(request):
    stories=[]
    for story in Story.objects.all().order_by("-id"):
        stories.append(story)
    data={
    "stories":stories,
    }
    return render(request, 'home.html', data)
