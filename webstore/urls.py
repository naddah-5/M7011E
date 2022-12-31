from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, about_us, Register, CreateProduct, ProductDetailView, AddToCartView

app_name = 'webstore'

urlpatterns = [
    path('', home, name = 'home'),
    path('about-us', about_us, name = 'about_us'),

    # Authorization
    path('register/', Register.as_view(), name = 'register'),
    path('login/', LoginView.as_view(template_name='pages/login.html'), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Admin
    path('product/create/', CreateProduct.as_view(), name='create_product'),

    # View
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),

    # Functions
    path('cart/add/<int:product_id>/', AddToCartView.as_view(), name='add_to_cart')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)