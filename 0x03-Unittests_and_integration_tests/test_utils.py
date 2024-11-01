#!/usr/bin/env python3
""" test for utils.access_nested_map """
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ class test case """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])


    def test_access_nested_map(self, nested_map, path, expected):
        """ >>> """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
        ])
    def test_access_nested_map_exception(self, nested_map, path, exception):
        """  test that a KeyError is raised for the following
        inputs (use @parameterized.expand): """
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
