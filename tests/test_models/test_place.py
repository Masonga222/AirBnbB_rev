#!/usr/bin/python3
"""
Tester class for the Place class
"""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    Tester definition
    """

    def __init__(self, *args, **kwargs):
        """
        class constructor
        """

        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        city id
        """

        new = self.value()
        self.assertEqual(type(new.city_id), type(new.city_id))

    def test_user_id(self):
        """
        user id
        """

        new = self.value()
        self.assertEqual(type(new.user_id), type(new.user_id))

    def test_name(self):
        """
        object name
        """

        new = self.value()
        self.assertEqual(type(new.name), type(new.name))

    def test_description(self):
        """
        testing description
        """

        new = self.value()
        self.assertEqual(type(new.description), type(new.description))

    def test_number_rooms(self):
        """
        number of the rooms
        """

        new = self.value()
        self.assertEqual(type(new.number_rooms), type(new.number_rooms))

    def test_number_bathrooms(self):
        """
        number of the bathrooms
        """

        new = self.value()
        self.assertEqual(type(new.number_bathrooms), type(
            new.number_bathrooms))

    def test_max_guest(self):
        """
        muximum guests
        """

        new = self.value()
        self.assertEqual(type(new.max_guest), type(new.max_guest))

    def test_price_by_night(self):
        """
        price per night
        """

        new = self.value()
        self.assertEqual(type(new.price_by_night), type(new.price_by_night))

    def test_latitude(self):
        """
        Latitude testing
        """

        new = self.value()
        self.assertEqual(type(new.latitude), type(new.latitude))

    def test_longitude(self):
        """
        Testing longitudes
        """

        new = self.value()
        self.assertEqual(type(new.longitude), type(new.longitude))

    def test_amenity_ids(self):
        """
        Is amenity there?
        """

        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
