from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.admin.views.decorators import staff_member_required

from .views import home, about_us, Register, CreateProduct, ProductDetailView, profile, add_to_cart, cart_summary, delete_from_cart, product_list, ProfileUpdate, get_categories, category_product_list, category_detail, sub_category, sub_category_detail, order, change_password

app_name = 'webstore'

urlpatterns = [
    path('', home, name = 'home'),
    path('about-us', about_us, name = 'about_us'),

    # Cart
    path('cart/', cart_summary, name="cart"),
    path('cart/add/<int:product_id>/', add_to_cart, name="add_to_cart"),
    path('cart/delete/<int:product_id>', delete_from_cart, name="delete_item"),

    # Order
    path('order/', order, name="order"),

    # Products
    path('product/', product_list, name="product_list"),
    path('product/<int:pk>/', ProductDetailView.as_view(extra_context={'categories': get_categories()}), name='product_detail'),   

    # Category
    path('category/', category_product_list, name="categories"),
    path('category/<int:category_id>', category_detail, name='category_details'),
    path('category/subcategory/', sub_category, name='sub-category'),
    path('category/subcategory/<int:sub_category_id>', sub_category_detail, name='sub_category_details'),

    # Authorization
    path('register/', Register.as_view(), name = 'register'),
    path('login/', LoginView.as_view(template_name='pages/login.html', extra_context={'categories': get_categories()}), name = 'login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/update/', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/change-password/', change_password, name='change_password'),
    
    # Admin
    path('product/create/', staff_member_required(CreateProduct.as_view()), name='create_product'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)