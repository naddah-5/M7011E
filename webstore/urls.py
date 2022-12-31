from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, about_us, Register, CreateProduct, ProductDetailView, product_details, profile, add_to_cart, cart_summary, delete_from_cart, product_list, ProfileUpdate

app_name = 'webstore'

urlpatterns = [
    path('', home, name = 'home'),
    path('about-us', about_us, name = 'about_us'),

    # Cart
    path('cart/', cart_summary, name="cart"),
    path('cart/add/<int:product_id>/', add_to_cart, name="add_to_cart"),
    path('cart/delete/<int:product_id>', delete_from_cart, name="delete_item"),

    # Order
    #path('order/',)

    # Products
    path('product/', product_list, name="product_list"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),   

    # Authorization
    path('register/', Register.as_view(), name = 'register'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', ProfileUpdate.as_view(), name='profile_update'),
    
    # Admin
    path('product/create/', CreateProduct.as_view(), name='create_product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)