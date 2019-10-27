from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def homepage(request, *args, **kwargs):
   # return HttpResponse("<h1>Hello World</h1>")
    return render(request, "home.html", {})

def list(request, *args, **kwargs):
    my_context = {
        "my_text": "Just attempt",
        "number": 123,
        "list": [1,5,7]
    }
    return render(request, "list.html", my_context)
