from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    template = loader.get_template('products/index.html')
    context = {
    'message': "Hello, world. You're at the products index."
    }
    return HttpResponse(template.render(context, request))
