from django.shortcuts import render
from django.http import HttpResponse
from .models import Bird

# class Bird:
#     def __init__(self, name, size, description):
#         self.name = name
#         self.size = size
#         self.description = description

# birds = [
#     Bird('House Finch', 'small', 'loves sunflower seeds, males are red'),
#     Bird('Dark Eyed Junco', 'small', 'scurries around the ground, eats millet, digs with its feet'),
# ]

# Create your views here.
def home(request):
    template = 'index.html'
    return render(request, template)

def birds_index(request):
    template = 'birds/index.html'
    birds = Bird.objects.all()
    context = {'birds': birds}
    return render(request, template, context)

def birds_detail(request, bird_id):
    # find bird by id
    bird = Bird.objects.get(id=bird_id)
    template = 'birds/detail.html'
    context = {'bird': bird}
    return render(request, template, context)