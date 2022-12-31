from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
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

def product_details(request):
    context = {
        'title': 'Product'
    }
    return render(request, 'pages/product_detail.html', context=context)

@login_required
def profile(request):
    user = request.user
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
    
    amount = 0
    if(userCart):
        amount = get_total_cart_sum(userCart)
    

    context = {
        'cart': userCart,
        'amount': amount
    }
    return render(request, 'pages/cart.html', context)

@login_required
def add_to_cart(request, **kwargs):

    quantity = 1

    if request.method == 'POST':
        quantity = int(request.POST['quantity'])

    user = request.user
    # get product from product ID that is going to get inserted to user cart
    # http://127.0.0.1:8000/add-to-cart/1 (1 describes the product id)
    product = Product.objects.filter(id=kwargs.get('product_id', "")).first()

    # Check stock
    if quantity>product.stock:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    userProduct, status = CartProduct.objects.get_or_create(user=user, product=product)

    if status:
        if quantity>1:
            userProduct.quantity += quantity
            userProduct.save()
        product.stock -= quantity
        product.save()
        print("Product id:" + str(kwargs.get('product_id', "")) + "has been added to user: " + str(user) + "s cart")
    else: 
        # the user already has this product in cart
        userProduct.quantity += quantity
        userProduct.save()
        product.stock -= quantity
        product.save()
        print("User already has this item...")
        print("User now has quantity amount:" + str(userProduct.quantity))

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def delete_from_cart(request, **kwargs):
    item = CartProduct.objects.filter(product_id=kwargs.get('product_id', "")).first()

    if item:
        item.product.stock += item.quantity
        item.delete()
        item.product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class ProductDetailView(DetailView):
    model = Product
    template_name = 'pages/product_detail.html'
    context_object_name = 'product'


def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def product_list(request):
    products = Product.objects.all()
    products = to_matrix(products, 4)
    
    context = {
        'products': products,
    }
    return render(request, "pages/products.html", context)

class ProfileUpdate(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserForm(initial={'username': request.user.username})
        user_profile_form = UserForm(
            initial={'username': request.user.username}
        )
        context = {
            'user_form': user_form,
            'user_profile_form': user_profile_form
        }
        return render(request, 'pages/update.html', context)

    def post(self, request):
        user_form = UserForm(request.POST, instance=request.user)
        user_profile_form = UserForm(request.POST,
                                            instance=request.user)
        if user_form.is_valid() and user_profile_form.is_valid():
            user_form.save()
            user_profile_form.save()
            return redirect('webstore:profile')

        context = {
            'user_form': user_form,
            'user_profile_form': user_profile_form
        }
        return render(request, 'pages/update.html', context)
