from django.shortcuts import render
from django.http import request

def home(request):

    context = {}
    return render(request,'index.html',context=context) 