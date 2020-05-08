from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    template = 'index.html'
    return render(request, template)

def birds_index(request):
    template = 'birds/index.html'
    # context = {'birds': birds}
    return render(request, template)