from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView

from webstore.forms import NewUserForm, UserForm
from webstore.models import Product

# Create your views here.
def home(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'pages/home.html', context=context)


# Create your views here.
def about_us(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'pages/about_us.html', context=context)

class Register(View):
    """
    Create a new user as well as the user profile.
    """
    
    def get(self, request):
        """
        Show the NewUserForm.
        """
        context = {
            'form': NewUserForm
        }
        return render(request, 'pages/register.html', context)

    def post(self, request):
        """
        Handles the submitted NewUserForm.
        """
        form = NewUserForm(request.POST)
        if form.is_valid():
            """
            Assuming that the data is valid, the new user is created and we redirect.
            """
            form.save()
            return redirect('/')
        
        context = {
            'form': form
        }
        """
        If the form is invalid we redirect back to the register page with the form as context.
        """
        return render(request, 'pages/register.html', context)

def product_details(request):
    context = {
        'title': 'Product'
    }
    return render(request, 'pages/product_detail.html', context=context)