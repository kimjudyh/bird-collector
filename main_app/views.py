from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Bird, Sighting, NestMaterial
from .forms import BirdForm, SightingForm, NestMaterialForm

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
    # show all nest materials that bird doesn't have
    materials_values_list = bird.nest_materials.all().values_list('id')
    unused_materials = NestMaterial.objects.exclude(id__in=materials_values_list)
    print('unused', unused_materials)
    # make the new sighting form available
    form = SightingForm()
    template = 'birds/detail.html'
    context = {
        'bird': bird,
        'form': form,
        'unused_materials': unused_materials,
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

def assoc_nest(request, bird_id, nest_material_id):
    """Associate or remove association between Bird and Nest Materials"""
    bird = Bird.objects.get(id=bird_id)
    nest_material = NestMaterial.objects.get(id=nest_material_id)
    print('nest material', nest_material)
    # check if Add or Remove button was clicked
    if request.POST.get('add_nest_material'):
        print('add')
        bird.nest_materials.add(nest_material)
    elif request.POST.get('remove_nest_material'):
        print('remove')
        bird.nest_materials.remove(nest_material)
    # redirect back to bird details page
    return redirect('detail', bird_id=bird_id)