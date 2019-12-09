from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Sighting
from django.http import HttpResponseRedirect
from .forms import AddForm

def index(request):
    sq_data = Sighting.objects.all()
    template = loader.get_template('sightings/index.html')
    context = {
                'sq_data': sq_data,
                }
    return HttpResponse(template.render(context, request))

def add(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = AddForm()

    return render(request, 'sightings/add.html', {'form':form})

def sqid(request, usid):
    squirrel_data = Sighting.objects.get(unique_squirrel_id = usid) 
    if request.method == 'POST':
        form = AddForm(request.POST, instance=squirrel_data)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings/')
    else:
        form = AddForm(instance = squirrel_data)
    return render(request, 'sightings/update.html', {'form':form})

# Create your views here.
