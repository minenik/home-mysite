from django.shortcuts import render
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse

def index(request):
   
    t = loader.get_template("index.html")
    c = Context({ 'posts': posts })
    return HttpResponse(t.render(c))
