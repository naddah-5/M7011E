from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, about_us, Register, CreateProduct, product_details, profile, add_to_cart, cart_summary, delete_from_cart

app_name = 'webstore'

urlpatterns = [
    path('', home, name = 'home'),
    path('about-us', about_us, name = 'about_us'),

    # Cart
    path('cart/', cart_summary, name="cart"),
    path('add-to-cart/<int:product_id>', add_to_cart, name="add_to_cart"),
    path('item/delete/<int:product_id>', delete_from_cart, name="delete_item"),

    # Order
    #path('order/',)

    # Authorization
    path('register/', Register.as_view(), name = 'register'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    
    # Admin
    path('product/create/', CreateProduct.as_view(), name='create_product'),

    # View
    path('product-detail/', product_details, name = 'product_details'),
]

urlpatterns += staticfiles_urlpatterns()