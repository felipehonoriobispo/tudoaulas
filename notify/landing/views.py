from django.shortcuts import render
from landing import views

# Create your views here.
def index(request):
    return render(request, "index.html")