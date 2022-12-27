"""
To make django look in this subdirectory for the models we need to import them to this __init__ file. 
If we for instance have a Breakfast model in a file breakfast.py that we want django to use we would import it like:

from .breakfast import Breakfast

I.e. we do:

from .<file (no .py)> import <class name>

"""

from .user_profile import UserProfile
from .order import Order
from .product import Product
from .order_product import OrderProduct
from .cart_product import CartProduct
from .review import Review
from .category import Category
from .subcategory import Subcategory
from .in_categorie import InCategorie
from .in_subcategory import InSubcategory