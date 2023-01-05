from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import HttpResponseRedirect, render, redirect, get_object_or_404
from django.views import View
from django.views.generic import CreateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView
from django.utils.timezone import now
from datetime import timedelta

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.admin.views.decorators import staff_member_required

from webstore.forms import NewUserForm, UserForm, ProductForm
from webstore.models import Product, CartProduct, Category, Subcategory, InCategory, InSubcategory, Order, OrderProduct, Video

def get_categories():
    categories = Category.objects.all()
    catDict = {}
    for cat in categories:
        try: #Category has sub category
            subCategories = Subcategory.objects.filter(category=cat).all()
            catDict[cat] = subCategories
        except: #Category does not have sub category
            catDict[cat] = []
    return catDict

# Create your views here.
def home(request):
    context = {
        'title': 'Home',
        'categories': get_categories(),
    }
    return render(request, 'pages/home.html', context=context)


# Create your views here.
def about_us(request):
    videos = Video.objects.all()


    context = {
        'videos': videos,
        'title': 'About Us',
        'categories': get_categories(),
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
            'form': NewUserForm,
            'categories': get_categories(),
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
            'form': form,
            'categories': get_categories(),
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


def get_order_price(id):
    order = Order.objects.filter(id=id).first()
    orderProducts = OrderProduct.objects.filter(order=order).all()

    amount = 0

    for item in orderProducts:
        amount += item.price

    return amount

def get_order_product(id):
    order = Order.objects.filter(id=id).first()
    orderProducts = OrderProduct.objects.filter(order=order).all()

    lst = []

    for item in orderProducts:
        lst.append(item)
    return lst


@login_required
def profile(request):
    user = request.user

    orders = Order.objects.filter(customer=user).all()

    lst = []

    for item in orders:
        lst.append([
            item.id,
            item.order_date,
            get_order_price(item.id),
            item.status,
            get_order_product(item.id),
        ])

    print(orders)



    context = {
        'order': lst,
        'user': user,
        'categories': get_categories(),
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
        'amount': amount,
        'categories': get_categories(),
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

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #product = Product.objects.filter(id=self.kwargs['pk'])
        categories = InCategory.objects.filter(product=self.model.objects.filter(id=self.kwargs['pk']).first()).all()
        catName = []
        for cat in categories:
            if(cat.product.name not in catName):
                catName.append(cat)

        context['category'] = catName
        return context

def to_matrix(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def product_list(request):
    products = Product.objects.all()

    lst = []
    for x in range(len(products)):
        lst.append([products[x].thumbnail.url, 
                    InCategory.objects.filter(product=products[x]).first(), 
                    products[x].id,
                    products[x].name,
                    products[x].price,
                    products[x].stock])

    products = to_matrix(lst, 4)

    context = {
        'products': products,
        'categories': get_categories(),
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
            'user_profile_form': user_profile_form,
            'categories': get_categories(),
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
            'user_profile_form': user_profile_form,
            'categories': get_categories(),
        }
        return render(request, 'pages/update.html', context)

def category_product_list(request):
    categories = Category.objects.all()

    categories = to_matrix(categories, 4)

    context = {
        'category': categories,
        'categories': get_categories(),
    }

    return render(request, 'pages/categories.html', context)

def category_detail(request, **kwargs):
    category = Category.objects.filter(id=kwargs.get('category_id', "")).first()
    print(category)

    products = InCategory.objects.filter(category=category)

    subCategories = Subcategory.objects.filter(category=category).all()

    lst = []
    for x in range(len(products)):
        try:
            lst.append([products[x].product.thumbnail.url, 
                        InCategory.objects.filter(product=products[x].product).first(), 
                        products[x].product.id,
                        products[x].product.name,
                        products[x].product.price,
                        products[x].product.stock])
        except:
            continue

    for x in range(len(subCategories)):
        try:
            subproduct = InSubcategory.objects.filter(subcategory=subCategories[x]).all()
            if(subproduct):
                for item in subproduct:
                    if(item.product not in products):
                        print(item.product.thumbnail.url)
                        lst.append([item.product.thumbnail.url, 
                                    InCategory.objects.filter(product=products[x].product).first(), 
                                    item.product.id,
                                    item.product.name,
                                    item.product.price,
                                    item.product.stock])
        except:
            print("X")
            continue

    lst = to_matrix(lst, 4)


    subCategories = to_matrix(subCategories, 4)
    
    

    context = {
        'products': lst,
        'subcategories': subCategories,
        'categories': get_categories(),
    }

    return render(request, 'pages/category_detail.html', context)

def sub_category(request):
    subCategories = Subcategory.objects.all()

    subCategories = to_matrix(subCategories, 4)

    context = {
        'category': subCategories,
        'categories': get_categories(),
    }

    return render(request, 'pages/subcategory.html', context)


def sub_category_detail(request, **kwargs):
    try:
        subCategories = Subcategory.objects.filter(id=kwargs.get('sub_category_id', "")).first()
        products = InSubcategory.objects.filter(subcategory=subCategories).all()
    except:
        pass

    lst = []

    for item in products:
        print(item.product.thumbnail.url)
        lst.append([item.product.thumbnail.url, 
        InCategory.objects.filter(product=item.product).first(), 
        item.product.id,
        item.product.name,
        item.product.price,
        item.product.stock])

    lst = to_matrix(lst, 4)

    context = {
        'products': lst,
        'categories': get_categories(),
    }
    return render(request, 'pages/subcategory_detail.html', context)

@login_required
def order(request):
    userCart = get_user_cart(request)

    print(userCart)

    amount = 0
    if(userCart):
        amount = get_total_cart_sum(userCart)

    if request.method == 'POST':
        order = Order.objects.create(
            order_date = now(),
            customer = request.user,
            address = request.POST.get('address'),
            delivery = now() + timedelta(days=5),
        )
        for item in userCart:
            orderProduct = OrderProduct.objects.create(
                product = item.product,
                order = order,
                quantity = item.quantity,
                price = item.product.price * item.quantity
            )
            item.delete()

    context = {
        'cart': userCart,
        'amount': amount,
        'categories': get_categories(),
    }

    return render(request, 'pages/order.html', context)

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request=request, user=request.user)
            return redirect(reverse("webstore:profile"))
        else:
            return redirect(reverse("webstore:change_password"))
    else:
        form = PasswordChangeForm(user=request.user)
        context = {
            'form': form
        }
        return render(request, 'pages/change_password.html', context)
 