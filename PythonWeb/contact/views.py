from django.shortcuts import render
from.import views
# Create your views here.
def getContact(request):
    return render(request, 'contact/contact.html')
