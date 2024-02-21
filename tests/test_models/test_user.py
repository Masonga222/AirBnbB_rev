#!/usr/bin/python3
"""
Class User test cases.
"""

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    Class definition
    """

    def __init__(self, *args, **kwargs):
        """Class constructor"""

        super().__init__(*args, **kwargs)
        self.name = "User"
        self.first_name = "User1"
        self.last_name = "Last"
        self.value = User

    def test_first_name(self):
        """
        Testing first name
        """

        new = self.value()
        self.assertEqual(type(new.first_name), type(new.first_name))

    def test_last_name(self):
        """
        Testing last name
        """

        new = self.value()
        self.assertEqual(type(new.last_name), type(new.last_name))

    def test_email(self):
        """
        Testing email
        """

        new = self.value()
        self.assertEqual(type(new.email), type(new.email))
