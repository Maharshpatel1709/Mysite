
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    # return HttpResponse("<h1>Hello World!</h1> <a href='https://www.youtube.com'>YouTube</a>")


def about(request):
    return HttpResponse("Hi! This is Maharsh")


def removepunc(request):
    djtext = request.GET.get('text', 'default')
    removepunc_check = request.GET.get('removepunc_check', 'off')
    if removepunc_check == 'on':
        punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed_text = ""
        for char in djtext:
            if char not in punctuations:
                analyzed_text += char
        params = {"purpose":"Removed Punctuations", "analyzed_text":analyzed_text}
        return render(request, "removepunc.html", params)
    else:
        return HttpResponse("Error")
