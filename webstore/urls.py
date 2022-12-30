from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView

from .views import home, about_us, Register, CreateProduct, ProductDetailView

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
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
]

urlpatterns += staticfiles_urlpatterns()