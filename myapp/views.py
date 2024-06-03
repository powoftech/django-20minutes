from django.http import HttpRequest
from django.shortcuts import HttpResponse, render

from myapp.models import TodoItem


# Create your views here.
def home(request: HttpRequest):
    return render(request, "home.html")


def todos(request: HttpRequest):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})
