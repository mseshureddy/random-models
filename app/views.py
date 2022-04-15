from pydoc_data.topics import topics
from django.shortcuts import render
from app.models import *

def display_topic(request):
    topics=Topic.objects.all()
    d={'ts':topics}
    return render(request,'display_topic.html',d)

def display_webpage(request):
    Web=Webpage.objects.all()
    d={'ws': Web}
    return render(request,'display_webpage.html',d)
# Create your views here.
