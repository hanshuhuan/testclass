from hmac import new
from operator import ne
from turtle import ht
from unittest import TestCase
from urllib import response
from django.shortcuts import render,redirect
from django.http import HttpResponse
from web.models import Item,List

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    else :
        username=request.POST.get("user")
        password=request.POST.get("pwd")
        # print(username,password)
        if username=="admin" and password=="123":
            return redirect("/index/")
        else:
            return render(request,"login.html",{"error":"用户名或密码错误"})

def photo_list(request):
    data=[
        {"name":"photo1","author":"author1"},
        {"name":"photo2","author":"author2"},
        {"name":"photo3","author":"author3"},
    ]
    return render(request,"photo_list.html",{"data":data})

def index(request):
    data=[
        {"name":"photo1","author":"author1"},
        {"name":"photo2","author":"author2"},
        {"name":"photo3","author":"author3"},
    ]
    return render(request,"index.html",{"data":data})

def home_page(request):
    return render(request,'home.html')
def view_list(request,list_id):
    list_user=List.objects.get(id=list_id)
    return render(request,'list.html',{'list':list_user})
def new_list(request):
    list_user=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_user)
    return redirect(f'/web/{list_user.id}/')
def add_item(request,list_id):
    list_user=List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_user)
    return redirect(f'/web/{list_user.id}/')
