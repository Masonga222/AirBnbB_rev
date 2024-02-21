#!/usr/bin/python3
"""
Test cases for the State class
"""

from models.base_model import BaseModel
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    Class tester definition
    """

    def test_State_inheritence(self):
        """
        Test that State class inherits from BaseModel.
        """

        new_state = State()
        self.assertIsInstance(new_state, BaseModel)

    def test_State_attributes(self):
        """
        Test that State class contains the attribute `name`.
        """

        new_state = State()
        self.assertTrue("name" in new_state.__dir__())

    def test_State_attributes_type(self):
        """
        Test that State class attribute name is class type str.
        """

        new_state = State()
        name = getattr(new_state, "name")
        self.assertIsInstance(name, str)
