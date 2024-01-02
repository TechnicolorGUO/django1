from django.shortcuts import render
from . import iot_mqtt
from .models import Event
# Create your views here.
def index(request):
    events = Event.objects.order_by('-date_created')
    context = {'events' : events} # Store the data in "context" dictionaries
    return render(request, 'iot/index.html', context) # Pass the context to HTML template

def log(request):
    events = Event.objects.order_by('-date_created')
    context = {'events' : events} # Store the data in "context" dictionaries
    return render(request, 'iot/log.html', context) # Pass the context to HTML template