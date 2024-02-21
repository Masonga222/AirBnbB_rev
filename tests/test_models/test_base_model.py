#!/usr/bin/python3
"""
Test Case for BaseModle class
"""

import sys
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """
    Tester definition
    """

    def __init__(self, *args, **kwargs):
        """
        Class constructor
        """

        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """
        Setting up
        """

        self.my_model = BaseModel()
        self.my_model.name = "Binita Rai"

    def tearDown(self):
        """
        Tearing down
        """

        del self.my_model

        try:
            os.remove('file.json')
        except TypeError:
            print("Invalid type")
        except FileNotFoundError:
            print("file.json not found")

    def test_id_type(self):
        """
        Checks that the type of the id is string.
        """

        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_differ(self):
        """
        Checks that the ids between two instances are different.
        """

        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_default(self):
        """
        Test case for default
        """

        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_name(self):
        """
        Checks that an attribute can be added.
        """

        self.assertEqual("Binita Rai", self.my_model.name)

    def test_kwargs(self):
        """
        Testing kwargs
        """

        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """
        testing kwargs ints
        """

        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """

        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """
        Testing strings
        """

        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """
        Testing to_dict method
        """

        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """
        Testing kwargs for None
        """

        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """
        Tesing id
        """

        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at1(self):
        """
        Testing created_at before update
        """

        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """
        Testing updated_at method
        """

        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_save(self):
        """
        Checks that after updating the instance; the dates
        differ in the updated_at attribute.
        """

        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update)

    def test_to_dict_class(self):
        """
        Checks that the __class__ key exists.
        """

        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        """
        Checks the type of the value of updated_at.
        """
        self.assertEqual("<class 'str'>", str(type((
            self.my_model.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):
        """
        Checks the type of the value of created_at.
        """

        tmp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs_instantiation(self):
        """
        Test that an instance is created using the
        key value pair.
        """

        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_type_created_at(self):
        """
        Test that the new_model's updated_at
        data type is datetime.
        """

        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_type_updated_at(self):
        """
        Test that the new_model's created_at
        data type is datetime.
        """

        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_compare_dict(self):
        """
        Test that the new_model's and my_model's
        dictionary values are same.
        """

        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(**my_model_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(my_model_dict, new_model_dict)

    def test_instance_diff(self):
        """
        Test that the my_model and new_model are
        not the same instance.
        """

        my_model_dict = self.my_model.to_dict()
        new_model = BaseModel(my_model_dict)
        self.assertNotEqual(self.my_model, new_model)
