from django.shortcuts import render
from .models import Item

# Create your views here.

def video(request):

    cc = Item.objects.all()
    return render(request, "index.html", {'cc': cc})

