from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.template import loader

from .models import *


def index(request):
    allEmployees = Employee.objects.all()
    template = loader.get_template('index.html')
    context = {
        'a': allEmployees,
    }
    return HttpResponse(template.render(context, request))


def post_index(request):
    if request.method == 'POST':
        a = Employee()
        a.pib = request.POST['pib']
        a.role = request.POST['role']
        a.salary = request.POST['salary']
        a.requirenments = request.POST['requirenments']
        Employee.save(a)
    return redirect('index')