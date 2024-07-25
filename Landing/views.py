from django.shortcuts import render

# Create your views here.

def landing(request):
    return render(request,'Landing/index.html',context={})