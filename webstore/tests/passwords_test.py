from django.test import TestCase
from models import Passwords

class PasswordsTest(TestCase):
    def test_create_password(self) -> None:
        new_password: Passwords = Passwords.objects.create(
            hash = "ijnfdoaisodiunasd"
        )
