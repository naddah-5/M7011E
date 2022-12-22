from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .views import home, about_us, login, register, product_details

app_name = 'webstore'

urlpatterns = [
    path('', home, name = 'home'),
    path('about-us', about_us, name = 'about_us'),
    path('login', login, name = 'login'),
    path('register', register, name = 'register'),
    path('product-detail', product_details, name = 'product_details'),
]

urlpatterns += staticfiles_urlpatterns()