from django.shortcuts import render
from .models import Item, Details
from django.http import HttpResponse
from .forms import ContactForm
# Create your views here.

def squad(request):
    cc = Item.objects.all()
    return render(request, "index.html", {'cc': cc})

def contactus(request):
    if request.method == 'POST':
        contact = Details()
        form_class = ContactForm
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()
        return HttpResponse("Thanks for contacting us ")
    return render(request, 'index.html', {
        'form': form_class ,
    })





