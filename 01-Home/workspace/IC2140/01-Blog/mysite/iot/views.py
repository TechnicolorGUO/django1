from django.shortcuts import render
from . import iot_mqtt
# Create your views here.
def index(request):
    return render(request, 'iot/index.html')