from django.test import TestCase
from django.db import models
from webstore.models import Users
from webstore.models.queries import create_user as db

import datetime

class UsersTests(TestCase):

    def test_create_user_email(self) -> None:
        db.create_new_user(
            user_email="testuser@hotmail.com", 
            given_create_time=datetime.datetime.now(), 
            set_role="CM"
        )
        created_user: Users = Users.objects.get(email = "testuser@hotmail.com")
        self.assertEqual(created_user.email, "testuser@hotmail.com")

    def test_create_user_unique(self) -> None:
        
        _: bool = db.create_new_user(
            user_email="testuser@hotmail.com",
            given_create_time=datetime.datetime.now(),
            set_role="CM"
        )
        same_user: bool = db.create_new_user(
            user_email="testuser@hotmail.com",
            given_create_time=datetime.datetime.now(),
            set_role="CM"
        )
        
        self.assertFalse(same_user)