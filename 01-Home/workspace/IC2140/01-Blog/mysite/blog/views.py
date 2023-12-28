from django.shortcuts import render
from .models import Entry
# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def blog(request):
    entries = Entry.objects.order_by('-date_posted')
    context = {'entries' : entries} # Store the data in "context" dictionaries
    return render(request, 'blog/blog.html', context) # Pass the context to HTML template