#!/usr/bin/env python3
""" test for utils.access_nested_map """
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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


class TestGetJson(unittest.TestCase):
    """ class and implement the TestGetJson.test_get_json method to test
    that utils.get_json returns the expected result."""
    

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
        ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """..."""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Implement the TestMemoize(unittest.TestCase)
    class with a test_memoize method."""


    def test_memoize(self):
        """..."""

        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()


        test_obj = TestClass()

        with patch.object(test_obj, 'a_method', return_value=42) as mock_method:
            self.assertEqual(test_obj.a_property, 42)
            self.assertEqual(test_obj.a_property, 42)

            mock_method.assert_called_once()
