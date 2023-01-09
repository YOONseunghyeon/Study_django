from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse
# Create your views here.
topics = [
    {'title' : '동아대학교', 'data' : 'images/img1.jpg', 'price' : 15000},
    {'title' : '꽃', 'data' : 'images/img2.jpg', 'price' :20000},
    {'title' : '부산대교', 'data' : 'images/img3.jpg', 'price' : 25000}
]


def index(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

def shop(request):
    global topics
    template = loader.get_template("shop.html")
    context = {
        "t" : topics,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    return HttpResponse("<h1>안녕하세여...create입니다~~~</h1>")

def read(request,id):
    return HttpResponse("<h1>안녕하세여...read입니다~~~</h1>"+id)

def datalist(request):
    m = Members.objects.all().values()
    context = {
    'm' : m,
    }
    template = loader.get_template('list.html')
    return HttpResponse(template.render(context,request))

def add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({},request))

def addrecord(request):
    x = request.POST["first"]
    y = request.POST["last"]
    m = Members(firstname=x, lastname=y)
    m.save()
    return HttpResponseRedirect(reverse("list"))

def delete(request,id):
    m =Members.objects.get(id=id)
    m.delete()
    return HttpResponseRedirect(reverse("list"))

def update(request,id):
    m= Members.objects.get(id=id)
    template = loader.get_template("update.html")
    context= {'m':m}
    return HttpResponse(template.render(context,request))

def updaterecord(request,id):
    m =Members.objects.get(id=id)
    x = request.POST["first"]
    y = request.POST["last"]
    m.firstname=x
    m.lastname=y
    m.save()
    return HttpResponseRedirect(reverse("list"))    