from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader

from .models import *


def index(request):
    a = A.objects.all()
    template = loader.get_template('index.html')
    context = {
        'a': a,
    }
    return HttpResponse(template.render(context, request))

def post_index(request):
    if request.method == 'POST':
        a = A()
        a.name = request.POST['name']
        a.description = request.POST['description']
        A.save(a)
    return redirect('index')