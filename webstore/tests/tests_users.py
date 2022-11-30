from django.test import TestCase
from webstore.models import Users

import datetime

class UsersTests(TestCase):

    def test_create_user(self) -> None:
        Users.objects.create(email="testuser@hotmail.com", create_time=datetime.datetime.now(), role="CM")
        created_user: Users = Users.objects.get(email = "testuser@hotmail.com")
        self.assertEqual(created_user.email, "testuser@hotmail.com")