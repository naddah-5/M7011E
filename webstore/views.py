from django.shortcuts import render

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

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # 

        print(username + " " + email)

    return render(request, 'pages/register.html')

def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        pass1 = request.POST["pass1"]

        # Authenticate och logga in
    return render(request, 'pages/login.html')

def product_details(request):
    context = {
        'title': 'Product'
    }
    return render(request, 'pages/product_detail.html', context=context)