from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from .models import team

# Create your views here.
def demo(request):
    obj=place.objects.all()
    ob=team.objects.all()
    return render(request,'index.html',{'result':obj,'res':ob})
# def addiction(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})