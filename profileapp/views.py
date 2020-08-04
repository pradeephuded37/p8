from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def trial(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"profileapp/home.html")

def profile(request):
    name="pradeep"
    contact='7204942247'
    emailid='pradeephuded37@gmail.com'
    return render(request,"profileapp/profile.html",{'name':name,'contact':contact,'emailid':emailid})