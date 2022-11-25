"""
To make django look in this subdirectory for the models we need to import them to this __init__ file. 
If we for instance have a Breakfast model in a file breakfast.py that we want django to use we would import it like:

from .breakfast import Breakfast

I.e. we do:

from .<file (no .py)> import <class name>

"""

from .passwords import Passwords
from .users import Users
from .orders import Orders
from .products import Products
from .order_product import OrderProducts
from .cart_product import CartProducts