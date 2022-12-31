from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView, DetailView

from webstore.forms import NewUserForm, UserForm, ProductForm
from webstore.models import Product, CartProduct

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

class CreateProduct(CreateView):
    form_class = ProductForm
    template_name = 'pages/create_product.html'
    # TODO: Add redirect to the added product.
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product_detail.html'
    context_object_name = 'product'

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        # Get product and quantity data from the form submission
        product_id = request.POST['product_id']
        quantity = request.POST['quantity']

        # Add the product to the cart


        # Redirect the user back to the product detail page
        return redirect('webstore:product_detail', product_id=product_id)