from django.urls import path

from .views import home, about_us, login, register

app_name = 'webstore'

urlpatterns = [
    path('', home, name = 'home'),
    path('about-us', about_us, name = 'about_us'),
    path('login', login, name = 'login'),
    path('register', register, name = 'register'),
]
