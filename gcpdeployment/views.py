from django.shortcuts import render, HttpResponse
from gcpdeployment.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'home.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact= Contact(name=name, email=email, phone=phone, message= message, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message sent succesfully.')
    return render(request, 'contact.html')

