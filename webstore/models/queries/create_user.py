import datetime
from webstore.models import Users, Passwords

def create_new_user(user_email: str, given_create_time: datetime.datetime, set_role: str) -> bool:
    try:
        Users(email = user_email, create_time = given_create_time, role = set_role).save()
        return True
    except:
        return False