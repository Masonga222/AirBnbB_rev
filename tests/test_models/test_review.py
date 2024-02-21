#!/usr/bin/python3
"""
Test cases for the Review class
"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    Class definition
    """

    def __init__(self, *args, **kwargs):
        """
        Class constructor
        """

        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """
        Test for Place Id
        """

        new = self.value()
        self.assertEqual(type(new.place_id), type(new.place_id))

    def test_user_id(self):
        """
        test for user id
        """

        new = self.value()
        self.assertEqual(type(new.user_id), type(new.user_id))

    def test_text(self):
        """
        Is text available?
        """

        new = self.value()
        self.assertEqual(type(new.text), type(new.text))
