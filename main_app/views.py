from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bird, Sighting
from .forms import BirdForm, SightingForm

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
    """Show Bird detail page"""
    # find bird by id
    bird = Bird.objects.get(id=bird_id)
    # make the new sighting form available
    form = SightingForm()
    template = 'birds/detail.html'
    context = {
        'bird': bird,
        'form': form,
        }
    return render(request, template, context)

def new_bird(request):
    """Add a new Bird"""
    # handle type of request
    # if a POST request is made
    if request.method == 'POST':
        # save the form data to database
        form = BirdForm(request.POST)
        if form.is_valid():
            # create new instance of bird
            bird = form.save()
            return redirect('detail', bird_id=bird.id)
    # if a GET request is made
    else:
        # render the form
        form = BirdForm()
        template = 'birds/new.html'
        context = {'form': form}
        return render(request, template, context)

def new_sighting(request, bird_id):
    """Add a new Sighting to a Bird"""
    form = SightingForm(request.POST)
    if form.is_valid():
        # assign bird_id to sighting, then save
        new_sighting = form.save(commit=False)
        new_sighting.bird_id = bird_id
        new_sighting.save()
    # redirect to bird's detail page
    return redirect('detail', bird_id=bird_id)