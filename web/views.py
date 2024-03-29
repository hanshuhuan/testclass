from django.shortcuts import render,redirect

from django.shortcuts import HttpResponse

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