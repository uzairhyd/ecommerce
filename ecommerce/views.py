from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    context = {
        'title': "Hello World",
        "content": "Welcome to the home page"
    }
    return render(request, 'home_page.html', context)

def about_page(request):
    context = {
        'title': "About Page",
        "content": "Welcome to the about page"
    }
    return render(request, 'home_page.html', context)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        'title': "Contact Page",
        "content": "Welcome to the contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, 'contact/view.html', context)

def login_page(request):
    return  render(request,"",{})

def register_page(request):
    return  render(request,"",{})