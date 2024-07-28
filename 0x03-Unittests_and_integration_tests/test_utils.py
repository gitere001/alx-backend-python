#!/usr/bin/env python3
"""test utils module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """test class for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
        Test the access_nested_map function with different inputs and expected
        outputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ["a"], KeyError),
        ({"a": 1}, ["a", "b"], KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_error):
        """
        Test the access_nested_map function with different inputs and expected
        outputs.
        """
        with self.assertRaises(expected_error):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Class for Testing Get Json """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Test for the utils.get_json function to check
        that it returns the expected result."""
        with patch('requests.get') as mock_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_get.return_value = mock_response

            # Call the function under test
            result = get_json(test_url)

            # Assertions
            self.assertEqual(result, test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Class for Testing Memoize """
    def test_memoize(self):
        """test memoize function"""
        class TestClass:
            """class for testing"""

            def a_method(self):
                """return 42"""
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method', return_value=42) as mock_obj:
            t = TestClass()
            result1 = t.a_property
            result2 = t.a_property
            result2 = t.a_property
            result2 = t.a_property
            result2 = t.a_property
            result2 = t.a_property
            result2 = t.a_property
            result2 = t.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_obj.assert_called_once()
