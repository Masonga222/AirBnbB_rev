#!/usr/bin/python3
"""
Tester for the City class
"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models.base_model import BaseModel


class test_City(test_basemodel):
    """
    Definition of the tester
    """

    def __init__(self, *args, **kwargs):
        """
        Class constructor
        """

        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Testing id
        """

        new = self.value()
        self.assertEqual(type(new.state_id), type(new.state_id))

    def test_name(self):
        """
        Testing object name
        """

        new = self.value()
        self.assertEqual(type(new.name), type(new.name))

    def test_City_inheritance(self):
        """
        tests that the City class Inherits from BaseModel
        """

        new_city = City()
        self.assertIsInstance(new_city, BaseModel)

    def test_User_attributes(self):
        """
        Testing user attributes
        """

        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())
