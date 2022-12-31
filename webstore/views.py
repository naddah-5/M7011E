from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
<<<<<<< HEAD
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
=======
from django.views.generic import CreateView, DetailView
>>>>>>> origin/69-product-page

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

<<<<<<< HEAD
def product_details(request):
    context = {
        'title': 'Product'
    }
    return render(request, 'pages/product_detail.html', context=context)

@login_required
def profile(request):
    user = request.user
    print(get_user_cart(request))
    context = {
        'user': user,
    }
    return render(request, 'pages/profile.html', context=context)

def get_user_cart(request):
    # get user
    user = request.user
    # filter CartProduct to get the users cart
    cart = CartProduct.objects.filter(user=user)
    if cart.exists():
        return cart
    return 0

def get_total_cart_sum(cart):
    total = 0
    for item in cart:
        total += item.product.price * item.quantity
    return total

@login_required
def cart_summary(request):
    userCart = get_user_cart(request)
    amount = get_total_cart_sum(userCart)
    print(amount)

    context = {
        'cart': userCart,
        'amount': amount
    }
    return render(request, 'pages/cart.html', context)

@login_required
def add_to_cart(request, quantity=1, **kwargs):
    user = request.user
    # get product from product ID that is going to get inserted to user cart
    # http://127.0.0.1:8000/add-to-cart/1 (1 describes the product id)
    product = Product.objects.filter(id=kwargs.get('product_id', "")).first()
    userProduct, status = CartProduct.objects.get_or_create(user=user, product=product)

    if status:
        userProduct.save()
        print("Product id:" + str(kwargs.get('product_id', "")) + "has been added to user: " + str(user) + "s cart")
    else: 
        # the user already has this product in cart
        userProduct.quantity += quantity
        userProduct.save()
        print("User already has this item...")
        print("User now has quantity amount:" + str(userProduct.quantity))

    return render(request, 'pages/profile.html')

@login_required
def delete_from_cart(request, **kwargs):
    item = CartProduct.objects.filter(product_id=kwargs.get('product_id', "")).first()
    if item:
        item.delete()
    return redirect(reverse('webstore:home'))
=======
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
>>>>>>> origin/69-product-page
