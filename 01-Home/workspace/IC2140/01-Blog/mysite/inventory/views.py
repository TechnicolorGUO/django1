from django.shortcuts import render, redirect
from .models import item
from datetime import datetime, timedelta
from django.db.models import Count

# Create your views here.
def index(request):
    entries = item.objects.all()
    context = {'items' : entries}
    return render(request, 'inventory/index.html', context) # Pass the context to HTML template

def inventory(request):
    current_date = datetime.now().date()
    five_years_ago = current_date - timedelta(days=5*365)
    e1 = item.objects.filter(price__gte = 10000) 
    e2 = item.objects.filter(purchase_date__lte=five_years_ago)
    e3= item.objects.values('loc').annotate(Count('id')).order_by('id__count')
    e4= item.objects.values('owner').annotate(Count('id')).order_by('id__count')
    context = {'con1':e1, 'con2':e2, 'con3':e3, 'con4':e4} # Store the data in "context" dictionaries
    return render(request, 'inventory/inventory.html', context) # Pass the context to HTML template



